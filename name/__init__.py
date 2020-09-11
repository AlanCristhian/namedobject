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
from typing import Iterator, Any, Optional, TypeVar, List
import sys


__all__ = ["AutoName"]
__version__ = "0.8.1"


_T = TypeVar("_T", bound="AutoName")
_STORE_INSTRUCTIONS = {
    4,    # DUP_TOP
    90,   # STORE_NAME
    97,   # STORE_GLOBAL
    125,  # STORE_FAST
    137,  # STORE_DEREF
    144,  # EXTENDED_ARG
}


class AutoName:
    def __init__(self) -> None:
        self.__name__ = "<nameless>"
        self._names: List[str] = []
        max_deepness = len(self.__class__.__mro__)
        frame: Optional[FrameType] = sys._getframe(1)
        for _ in range(max_deepness):
            if not frame:
                break
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
                break
            else:
                frame = frame.f_back

    # I define the '__iter__' method to give compatibility
    # with the iterable unpacking syntax.
    def __iter__(self: _T) -> Iterator[_T]:
        for name in self._names:
            obj = self.__class__()
            obj.__name__ = name
            yield obj

    def __set_name__(self, owner: Any, name: str) -> None:
        self.__name__ = name

    def __enter__(self: _T) -> _T:
        return self

    def __exit__(*args: Any) -> Optional[bool]:
        pass
