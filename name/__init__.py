"""A library with a base class that stores the assigned name of an object.

>>> import name
>>> x, y = name.AutoName()
>>> x.__name__
'x'
>>> y.__name__
'y'
"""

from __future__ import annotations

from types import FrameType
from typing import Iterator, Any, Optional, TypeVar, List, Dict, Tuple
import sys


__all__ = ["AutoName"]
__version__ = "0.8.4"


_T = TypeVar("_T", bound="AutoName")
_STORE_INSTRUCTIONS = {
    4,    # DUP_TOP
    90,   # STORE_NAME
    97,   # STORE_GLOBAL
    125,  # STORE_FAST
    137,  # STORE_DEREF
    144,  # EXTENDED_ARG
}


def _get_frame(type_: type) -> Optional[FrameType]:
    deepness = len({
        t.__init__  # type: ignore[misc]
        for t in type_.__mro__
        if AutoName in t.__mro__
    })
    try:
        return sys._getframe(deepness + 1)
    except ValueError as error:
        if error.args == ('call stack is not deep enough',):
            return sys._getframe(deepness)
        else:
            raise error


class AutoName:
    def __new__(
        cls,
        *args: Tuple[Any, ...],
        **kwds: Dict[str, Any]
    ) -> "AutoName":
        obj: "AutoName" = super().__new__(cls)
        obj._autoname_args: Tuple[Any, ...] = args  # type: ignore[misc]
        obj._autoname_kwds: Dict[str, Any] = kwds  # type: ignore[misc]
        return obj

    def __init__(self) -> None:
        self._autoname_args: Tuple[Any, ...]
        self._autoname_kwds: Dict[str, Any]
        self.__name__ = "<nameless>"
        self._names: List[str] = []
        frame = _get_frame(self.__class__)
        try:
            if not frame:
                return
            store_opcode = {
                90: frame.f_code.co_names,      # STORE_NAME
                97: frame.f_code.co_names,      # STORE_GLOBAL
                125: frame.f_code.co_varnames,  # STORE_FAST
                137: frame.f_code.co_cellvars,  # STORE_DEREF
            }
            bytecode = frame.f_code.co_code
            start = frame.f_lasti + 2
            stop = len(bytecode)
            extended_arg = 0
            for i in range(start, stop, 2):
                instruction = bytecode[i]
                if instruction == 92:  # UNPACK_SEQUENCE
                    continue
                elif instruction == 144:  # EXTENDED_ARG
                    extended_arg |= bytecode[i + 1] << 8
                elif instruction in store_opcode:
                    index = extended_arg | bytecode[i + 1]
                    name = store_opcode[instruction][index]
                    self._names.append(name)
                if self._names:
                    if instruction not in _STORE_INSTRUCTIONS:
                        break
            if self._names:
                self.__name__ = self._names[-1]
        finally:
            del frame

    # I define the '__iter__' method to give compatibility
    # with the iterable unpacking syntax.
    def __iter__(self: _T) -> Iterator[_T]:
        for name in self._names:
            obj = self.__class__(  # type: ignore[call-arg]
                *self._autoname_args,
                **self._autoname_kwds
            )
            obj.__name__ = name
            yield obj

    def __set_name__(self, owner: Any, name: str) -> None:
        self.__name__ = name

    def __enter__(self: _T) -> _T:
        return self

    def __exit__(*args: Any) -> Optional[bool]:
        pass
