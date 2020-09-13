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
import copy


__all__ = ["AutoName"]
__version__ = "0.8.5"


_T = TypeVar("_T", bound="AutoName")


# Instructions related with store the name of an object somewhere.
_ALLOWED_INSTRUCTIONS = {
    4,    # DUP_TOP
    90,   # STORE_NAME
    97,   # STORE_GLOBAL
    125,  # STORE_FAST
    137,  # STORE_DEREF
    144,  # EXTENDED_ARG
}


# Get the frame where the object was created
# to search the name of such object there.
def _get_frame(type_: type) -> Optional[FrameType]:

    # The call stack deepnes increases each time that the user
    # make a subclass of AutoName and override the __init__
    # method. So, it count how many times __init__ was overrided.
    deepness = len({
        t.__init__  # type: ignore[misc]
        for t in type_.__mro__
        if AutoName in t.__mro__
    })
    try:

        # Deepnes is plus one because the current funcion add a frame
        return sys._getframe(deepness + 1)
    except ValueError as error:
        if error.args == ('call stack is not deep enough',):

            # There is a case where if the user define a subclass of AutoName
            # in the main global namespace, then the deepness is the same than
            # before minus one. But since the current function add one, just
            # use the original value obtained.
            return sys._getframe(deepness)
        raise error


class AutoName:
    def __init__(self) -> None:
        self.__name__ = "<nameless>"

        # Python can create many names with iterable unpacking syntax and
        # multiple assignment syntax. That is why it store them all.
        self._names: List[str] = []
        frame = _get_frame(self.__class__)
        try:
            if not frame:
                return
            STORED_NAMES = {
                90: frame.f_code.co_names,      # STORE_NAME
                97: frame.f_code.co_names,      # STORE_GLOBAL
                125: frame.f_code.co_varnames,  # STORE_FAST
                137: frame.f_code.co_cellvars,  # STORE_DEREF
            }
            bytecode = frame.f_code.co_code

            # f_lasti indicates the position of the last bytecode instruction.
            # In this case, it is the call to the class. So, it skip them and
            # start in the next opcode. That one is two step ahead.
            start = frame.f_lasti + 2
            stop = len(bytecode)
            extended_arg = 0

            # Every Python instruction takes 2 bytes. The first byte represent
            # the instruction, and the second byte is their argument. That is
            # why the loop step is 2.
            #
            # The argument is also used to compute the index of name in the
            # attribute co_* of frame.f_code.
            for i in range(start, stop, 2):
                instruction = bytecode[i]
                if instruction == 92:  # UNPACK_SEQUENCE
                    continue
                elif instruction == 144:  # EXTENDED_ARG
                    extended_arg |= bytecode[i + 1] << 8  # compute the index
                elif instruction in STORED_NAMES:
                    index = extended_arg | bytecode[i + 1]
                    name = STORED_NAMES[instruction][index]
                    self._names.append(name)
                if self._names:
                    if instruction not in _ALLOWED_INSTRUCTIONS:
                        break
            if self._names:

                # In both cases where the user want to use single assignment
                # or multiple assigments, the correct name is the last one.
                #
                # Why the last, and not the first? Because that is how
                # __set_name__ behaves in the same situation.
                self.__name__ = self._names[-1]
        finally:
            del frame

    # The '__iter__' method is defined to give compatibility
    # with iterable unpacking syntax.
    def __iter__(self: _T) -> Iterator[_T]:
        for name in self._names:
            instance = copy.copy(self)
            instance.__name__ = name
            yield instance

    def __set_name__(self, owner: Any, name: str) -> None:
        self.__name__ = name

    def __enter__(self: _T) -> _T:
        return self

    def __exit__(*args: Any) -> Optional[bool]:
        pass
