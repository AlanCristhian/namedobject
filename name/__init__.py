"""A library with a base class that stores the assigned name of an object.

>>> import name
>>> a = name.AutoName()
>>> a.__name__
'a'
"""

from __future__ import annotations

from types import FrameType, ModuleType
from typing import Generator, Iterator, Dict, Any, Optional, List, Union
import sys


__all__ = ["AutoName"]
__version__ = "0.2.2"


_FrameGenerator = Generator[Dict[str, Any], None, None]


_NOT_FOUND_EXCEPTION = NameError("Can not be found the name of this object.")


# Yields all locals variables in the higher (calling) frames
def _get_outer_locals(frame: Optional[FrameType]) -> _FrameGenerator:
    while frame:
        yield frame.f_locals
        frame = frame.f_back


# Get the path of the module where the AutoName instance has been defined
def _get_module_path() -> Union[str, None]:
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
        scopes = []

        for variables in _get_outer_locals(frame):

            # NOTE 3: An object could have various names in the same scope. So,
            # I stores all in the 'names' var. This situation happen when user
            # assign the object to multiples variables with the "multiple
            # assignment syntax".
            names: List[str] = []
            variables_items = iter(variables.items())
            for name, value in variables_items:
                len_names = self._search_recursively(value, names, name)

                # NOTE 4: since python 3.6, dictionaries remember the order of
                # items inserted. And since 3.7 that behaviour are a intended
                # feature. Because that, when the user make a multiple
                # assignment, python stores each name close to each other. So,
                # to know if the user has made a multiple assignment is
                # enought to check if the next name is the object, then stop.
                if len_names:
                    try:
                        name, value = next(variables_items)
                    except StopIteration:
                        pass
                    else:
                        if value is self:
                            names.append(name)
                    finally:
                        break

            if names:
                scopes.append(names)
        if scopes:

            # Remember: the valid name is one that is in the last scope.
            names = scopes[-1]
            if len(names) > 1:  # Check for multiple assignment.
                raise NameError(
                    "Can not assign multiples names to the same object.")
            else:
                return names[0]
        raise _NOT_FOUND_EXCEPTION

    def _search_recursively(
        self,
        value: Any,
        names: List[str],
        name: str,
    ) -> int:

        # search the name in the frame
        if value is self:
            names.append(name)

        # Search the name in a namespace
        elif isinstance(value, type):
            key_val = iter(vars(value).items())
            for key, val in key_val:
                if val is self:
                    names.append(key)
                    break

            # See NOTE 4
            try:
                key, val = next(key_val)
            except StopIteration:
                pass
            else:
                if val is self:
                    names.append(key)

        # Search the name in a module
        elif isinstance(value, ModuleType):
            if hasattr(value, "__file__"):
                if value.__file__ not in {None, self._module}:
                    return len(names)
                for key, val in vars(value).items():
                    len_names = self._search_recursively(val, names, key)
                    if len_names > 1:
                        break
        return len(names)

    @property
    def __name__(self) -> str:
        """Search the name of the instance of the current class."""
        if self._name is None:
            frame: Optional[FrameType] = sys._getframe(1)
            if frame is None:
                raise _NOT_FOUND_EXCEPTION
            else:
                self._name = self._search_name(frame)
        return self._name
