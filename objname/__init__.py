"""A library with a base class that stores the assigned name of an object.

>>> x, y = AutoName()
>>> x.name
'x'
>>> y.name
'y'
"""

from collections import deque
from types import FrameType
from typing import Iterator, Optional, TypeVar, List, Deque, Tuple, Any, Dict
import opcode
import sys


__all__ = ["AutoName"]
__version__ = "0.12.1"


# Get opcode numeric values from the opcode library
# because that numbers can change between versions
_EXTENDED_ARG = opcode.opmap["EXTENDED_ARG"]
_STORE_NAME = opcode.opmap["STORE_NAME"]
_STORE_ATTR = opcode.opmap["STORE_ATTR"]
_STORE_GLOBAL = opcode.opmap["STORE_GLOBAL"]
_STORE_FAST = opcode.opmap["STORE_FAST"]
_STORE_DEREF = opcode.opmap["STORE_DEREF"]


_T = TypeVar("_T", bound="AutoName")


# Instructions related with store the name of an object somewhere.
_ALLOWED_INSTRUCTIONS = {
    _EXTENDED_ARG,
}


# Some opcodes has been deleted, and some others has been added.
# So I need to check wich python version to fill the following set.
if sys.version_info >= (3, 11, 0, "alpha", 0):
    _ALLOWED_INSTRUCTIONS.add(opcode.opmap["COPY"])
    _ALLOWED_INSTRUCTIONS.add(opcode.opmap["CACHE"])
else:
    _ALLOWED_INSTRUCTIONS.add(opcode.opmap["DUP_TOP"])


# Get the frame where the object was created
# to search the name of such object there.
def _get_frame(deepness: int) -> Optional[FrameType]:
    try:

        # Deepness is plus one because the current funcion add a frame
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
    """Stores the assigned name of an object.

    Single assignment:
    >>> obj = AutoName()
    >>> obj.name
    'obj'

    Iterable unpacking syntax:
    >>> a, b = AutoName()
    >>> a.name
    'a'
    >>> b.name
    'b'
    """

    _deepness: int = 1
    _args: Tuple[Any, ...]
    _kwargs: Dict[str, Any]
    name = "<nameless>"

    def __new__(
        cls,
        *args: Tuple[Any, ...],
        **kwargs: Dict[str, Any]
    ) -> "AutoName":
        new_obj: AutoName = super().__new__(cls)
        new_obj._args = args
        new_obj._kwargs = kwargs
        return new_obj

    def __init__(self) -> None:
        frame = _get_frame(self._deepness)
        if frame:
            if frame.f_code.co_name == "__iter__":
                return
        else:
            return

        # Here it will be stored the names needed
        # for the iterable unpacking syntax.
        self._iterable_names: Deque[List[str]] = deque()

        # Python can create many names with iterable unpacking syntax and
        # multiple assignment syntax. That is why it store them all.
        multiple_names: List[str] = []
        slices: List[Tuple[int, int]] = []
        delta = 0
        try:
            STORED_NAMES = {
                _STORE_NAME: frame.f_code.co_names,
                _STORE_ATTR: frame.f_code.co_names,
                _STORE_GLOBAL: frame.f_code.co_names,
                _STORE_FAST: frame.f_code.co_varnames,
                _STORE_DEREF: frame.f_code.co_cellvars,
            }
            VARNAME_FROM_OPARG = (
                STORED_NAMES[_STORE_FAST] + STORED_NAMES[_STORE_DEREF])
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

                    # count is the amount of variables that want to unpack
                    count = extended_arg | bytecode[i + 1]
                    extended_arg = 0

                    # Store slices because names that will
                    # be used are not known at this point.
                    begin = len(multiple_names)
                    end = begin + count
                    slice_ = (begin - delta, end - delta)
                    slices.append(slice_)
                    delta = end - begin
                elif instruction == 144:  # EXTENDED_ARG
                    extended_arg |= bytecode[i + 1] << 8  # compute the index
                elif instruction in STORED_NAMES:
                    index = extended_arg | bytecode[i + 1]
                    extended_arg = 0
                    try:
                        name = STORED_NAMES[instruction][index]

                    # Following error happens on python 3.11
                    except IndexError as error:
                        if hasattr(frame.f_code, "_varname_from_oparg"):
                            name = VARNAME_FROM_OPARG[index]
                        else:
                            raise error
                    multiple_names.append(name)
                elif multiple_names:
                    if instruction not in _ALLOWED_INSTRUCTIONS:
                        break

            # Iterable unpacking syntax
            if slices:
                for begin, end in slices:

                    # Store names that will be used in iterable unpacking
                    names = multiple_names[begin:end]
                    self._iterable_names.append(names)

                    # Remove unneeded names that will be
                    # used in single or multiple assignment
                    del multiple_names[begin:end]

            # Multiple and single assignment syntax
            if multiple_names:

                # [NOTE 1]: The correct name is the last one because
                # that is how __set_name__ behaves in the same situation.
                self.name = multiple_names[-1]
        finally:
            del frame

    # The '__iter__' method is defined to give compatibility
    # with iterable unpacking syntax.
    def __iter__(self: _T) -> Iterator[_T]:
        for name in self._iterable_names.popleft():
            instance = type(self)(
                *self._args, **self._kwargs)
            instance.name = name
            yield instance

    def __init_subclass__(cls) -> None:

        # The call stack deepness increases each time that the user
        # make a subclass of AutoName and override the __init__
        # method. So, it count how many times __init__ was overrided.
        cls._deepness = len({
            t.__init__  # type: ignore[misc]
            for t in cls.__mro__
            if AutoName in t.__mro__
        })
        super().__init_subclass__()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
