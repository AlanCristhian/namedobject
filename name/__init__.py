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
__version__ = "0.6.0"


_FrameGenerator = Generator[Dict[str, Any], None, None]
_T = TypeVar("_T", bound="AutoName")


# Yields all locals variables in the higher (calling) frames
def _get_outer_locals(frame: Optional[FrameType]) -> _FrameGenerator:
    while frame:
        yield frame.f_locals
        frame = frame.f_back


# Get the path of the module where the AutoName instance has been defined
def _get_module_path() -> Any:
    frame: FrameType = sys._getframe(2)
    while frame.f_code.co_name != "<module>":
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

        # I call 'type(self)' to warranty that __iter__
        # method works even in a subclass of AutoName.
        return (type(self)() for _ in range(self._count))

    def _search_in_module(self) -> str:
        module = sys.modules[self._module_path]
        for name, value in reversed(vars(module).items()):
            if value is self:
                return name
        return "<nameless>"

    def _search_in_frames(self) -> str:
        frame: Optional[FrameType] = sys._getframe(2)
        last_name = "<nameless>"
        name_seen = "<nameless>"
        for variables in _get_outer_locals(frame):

            # When a user assign an object to several variables with
            # the "multiple assignment syntax", that object will have
            # more than one name. The valid name is the last, that's
            # why y reverse the 'variables' dictionary.
            for name, value in reversed(variables.items()):
                if value is self:
                    last_name = name
                    break

            # The same object could have many names in
            # differents scopes. The valid name is the one
            # that is the same than the precedent scope.
            if last_name == name_seen:
                return last_name
            else:
                name_seen = last_name

        return "<nameless>"

    @property
    def __name__(self) -> str:
        """Search the name of the instance of the current instance."""
        if self._name is None:
            if self._module_path == "__main__":
                self._name = self._search_in_frames()
            else:
                self._name = self._search_in_module()
        return self._name

    def __set_name__(self, owner: Any, name: str) -> None:
        self._name = name

    def __enter__(self: _T) -> _T:
        return self

    def __exit__(*args: Any) -> Optional[bool]:
        pass
