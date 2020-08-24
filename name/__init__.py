"""A library with a base class that stores the assigned name of an object.

>>> import name
>>> a = name.AutoName()
>>> a.__name__
'a'
"""

from __future__ import annotations

from types import FrameType
from typing import Generator, Iterator, Dict, Any, Optional, TypeVar, Set
import sys

__all__ = ["AutoName"]
__version__ = "0.5.6"


_FrameGenerator = Generator[Dict[str, Any], None, None]
_T = TypeVar("_T", bound="AutoName")


_NOT_FOUND_ERROR = NameError("The name of this object has not been found.")


# Yields all locals variables in the higher (calling) frames
def _get_outer_locals(frame: Optional[FrameType]) -> _FrameGenerator:
    while frame:
        yield frame.f_locals
        frame = frame.f_back


# Get the path of the module where the AutoName instance has been defined
def _get_module_path() -> Any:
    frame: FrameType = sys._getframe(2)
    while "__name__" not in frame.f_locals:
        frame = frame.f_back  # type: ignore
    return frame.f_locals["__name__"]


class AutoName:
    """ Creates an object that stores the name of itself.

    >>> import name
    >>> a = name.AutoName()
    >>> a.__name__
    'a'

    It can also creates multiples variables using the unpack sequence syntax.
    To do that you must pass the amount of object that you want as argument.

    >>> import name
    >>> a, b, c = name.AutoName(3)
    >>> a.__name__
    'a'
    >>> b.__name__
    'b'
    >>> c.__name__
    'c'

    """
    def __init__(self, count: int = 1):
        assert count >= 1, "Expected positive 'int' number, got '%r'" % count
        self._count = count
        self._name: Optional[str] = None
        self._module_path = _get_module_path()

    # I define the '__iter__' method to give compatibility
    # with the unpack sequence assignment syntax.
    def __iter__(self: _T) -> Iterator[_T]:

        # NOTE 1: I call 'type(self)' to warranty that it
        # method works even in a subclass of this.
        return (type(self)() for _ in range(self._count))

    # Search the assigned name of the current object.
    def _search_name(self, frame: Optional[FrameType]) -> str:

        # for module in modules:
        if self._module_path != "__main__":
            module = sys.modules[self._module_path]
            for name, value in reversed(vars(module).items()):
                if value is self:
                    return name

        # Search the name in all frames
        last_name: Optional[str] = None
        names: Set[Optional[str]] = set()
        for variables in _get_outer_locals(frame):

            # NOTE 2: An object could have various names in the same scope. So,
            # I stores all in the 'names' var. This situation happen when user
            # assign the object to multiples variables with the "multiple
            # assignment syntax".
            for name, value in reversed(variables.items()):
                if value is self:
                    last_name = name
                    break

            # NOTE 3: The same object could have many names in differents
            # scopes. The valid name is the one that is in the last scope.
            # If the name is the same than the precedent scope, then I can
            # break the loop.
            if last_name in names:
                break
            else:
                names.add(last_name)
        if last_name:
            return last_name

        raise _NOT_FOUND_ERROR

    @property
    def __name__(self) -> str:
        """Search the name of the instance of the current instance."""
        if self._name is None:
            frame: Optional[FrameType] = sys._getframe(1)
            if frame:
                self._name = self._search_name(frame)
            else:
                raise _NOT_FOUND_ERROR
        return self._name

    def __set_name__(self, owner: Any, name: str) -> None:
        self._name = name

    def __enter__(self: _T) -> _T:
        return self

    def __exit__(*args: Any) -> Optional[bool]:
        pass
