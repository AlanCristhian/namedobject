"""A library with a base class that stores the assigned name of an object.

>>> import name
>>> a = name.AutoName()
>>> a.__name__
'a'
"""

from __future__ import annotations

from types import FrameType
from typing import Generator, Iterator, Dict, Any, Optional, TypeVar
import sys


__all__ = ["AutoName"]
__version__ = "0.7.0"


_FrameGenerator = Generator[Dict[str, Any], None, None]
_T = TypeVar("_T", bound="AutoName")
_ALLOWED = {
    4,    # DUP_TOP
    90,   # STORE_NAME
    97,   # STORE_GLOBAL
    125,  # STORE_FAST
    137,  # STORE_DEREF
    144,  # EXTENDED_ARG
}


class AutoName:
    def __init__(self, count: int = 1):
        assert count >= 0, "Expected positive 'int' number, got '%r'" % count
        self.__name__ = "<nameless>"
        if count == 0:
            return
        self._names = []
        frame: Optional[FrameType] = sys._getframe(1)
        max_deepness = len(type(self).__mro__)
        extended_arg = bytearray()
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
            start = frame.f_lasti + (2 if count == 1 else 4)
            for i in range(start, len(bytecode), 2):
                instruction = bytecode[i]
                if instruction == 144:  # EXTENDED_ARG
                    extended_arg.append(bytecode[i + 1])
                elif instruction in store_opcode:
                    extended_arg.append(bytecode[i + 1])
                    index = int.from_bytes(extended_arg, "big")
                    name = store_opcode[instruction][index]
                    self._names.append(name)
                    extended_arg.clear()
                if self._names:
                    if instruction not in _ALLOWED:
                        break
            if self._names:
                self.__name__ = self._names[-1]
                break
            else:
                if extended_arg:
                    extended_arg.clear()
                frame = frame.f_back

    # I define the '__iter__' method to give compatibility
    # with the unpack sequence assignment syntax.
    def __iter__(self: _T) -> Iterator[_T]:
        for name in self._names:
            obj = type(self)(0)
            obj.__name__ = name
            yield obj

    def __set_name__(self, owner: Any, name: str) -> None:
        self.__name__ = name

    def __enter__(self: _T) -> _T:
        return self

    def __exit__(*args: Any) -> Optional[bool]:
        pass
