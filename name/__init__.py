"""A library with a base class that stores the assigned name of an object.

>>> import name
>>> a = name.AutoName()
>>> a.__name__
'a'
"""

from __future__ import annotations

from types import FrameType, ModuleType
from typing import Generator, Iterator, Dict, Any, Optional
import sys


__all__ = ["AutoName"]
__version__ = "0.3.0"


_FrameGenerator = Generator[Dict[str, Any], None, None]


_NOT_FOUND_ERROR = NameError("The name of this object has not been found.")


# Yields all locals variables in the higher (calling) frames
def _get_outer_locals(frame: Optional[FrameType]) -> _FrameGenerator:
    while frame:
        yield frame.f_locals
        frame = frame.f_back


# Get the path of the module where the AutoName instance has been defined
def _get_module_path() -> Optional[str]:
    frame = sys._getframe(2)
    while frame.f_locals is not frame.f_globals:
        frame = frame.f_back  # type: ignore
    return frame.f_locals.get("__file__")


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
    def __init__(self, count: int = 0):
        assert count >= 0, "Expected positive 'int' number, got '%r'" % count
        self._count = count
        self._name: Optional[str] = None
        self._module = _get_module_path()

    # I define the '__iter__' method to give compatibility
    # with the unpack sequence assignment syntax.
    def __iter__(self) -> Iterator[AutoName]:

        # NOTE 1: I call 'type(self)' to warranty that it
        # method works even in a subclass of this.
        return (type(self)() for _ in range(self._count))

    # Search the assigned name of the current object.
    def _search_name(self, frame: Optional[FrameType]) -> str:

        # NOTE 2: The same object could have many names in differents scopes.
        # So, I stores all names in the 'scopes' var. The valid name is one
        # that is in the last scope.
        last_name: Optional[str] = None

        for variables in _get_outer_locals(frame):

            # NOTE 3: An object could have various names in the same scope. So,
            # I stores all in the 'names' var. This situation happen when user
            # assign the object to multiples variables with the "multiple
            # assignment syntax".
            for key, value in variables.items():
                name = self._search_recursively(value, key)
                if name:
                    last_name = name
                    break
        if last_name:
            return last_name
        raise _NOT_FOUND_ERROR

    def _search_recursively(self, value: Any, name: str,) -> Optional[str]:

        # search the name in the frame
        if value is self:
            return name

        # Search the name in a module
        elif isinstance(value, ModuleType):
            if hasattr(value, "__file__"):
                if value.__file__ not in {None, self._module}:
                    return None
                for key, val in vars(value).items():
                    new_name = self._search_recursively(val, key)
                    if new_name:
                        return new_name
        return None

    @property
    def __name__(self) -> str:
        """Search the name of the instance of the current class."""
        if self._name is None:
            frame: Optional[FrameType] = sys._getframe(1)
            if frame:
                self._name = self._search_name(frame)
            else:
                raise _NOT_FOUND_ERROR
        return self._name

    def __get__(self, instance: Any, owner: Any) -> "AutoName":
        """Search the name of the attribute of the current class."""
        if self._name is None:
            self._name = next(k for k, v in vars(owner).items() if v is self)
        return self
