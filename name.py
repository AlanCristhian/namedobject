"""A library with a base class that stores the assigned name of an object.

>>> import name
>>> a = name.AutoName()
>>> a.__assigned_name__
'a'
"""

from __future__ import annotations

from types import FrameType, ModuleType
from typing import Generator, Iterator, Dict, Any, Optional, List, Set
import inspect

import name as namemodule


__all__ = ["AutoName"]
__version__ = "0.1.2"


_FrameGenerator = Generator[Dict[str, Any], None, None]


_NOT_FOUND_EXCEPTION = NameError("Can not be found the name of this object.")
_modules_with_autoname_instances = set()


# Yields all locals variables in the higher (calling) frames
def _get_outer_locals(frame: Optional[FrameType]) -> _FrameGenerator:
    while frame:
        yield frame.f_locals
        frame = frame.f_back


class AutoName:
    """ Creates an object that stores the name of itself.

    >>> import name
    >>> a = name.AutoName()
    >>> a.__assigned_name__
    'a'

    It can also creates multiples variables using the unpack sequence syntax.
    To do that you must pass the amount of object that you want as argument.

    >>> import name
    >>> a, b, c = name.AutoName(3)
    >>> a.__assigned_name__
    'a'
    >>> b.__assigned_name__
    'b'
    >>> c.__assigned_name__
    'c'

    """
    def __init__(self, count: int = 0):
        assert count >= 0, "Expected positive 'int' number, got '%r'" % count
        self.__count = count
        self.__name: Optional[str] = None
        _modules_with_autoname_instances.add(
            inspect.currentframe().f_back.f_globals["__file__"])  # type:ignore

    # I define the '__iter__' method to give compatibility
    # with the unpack sequence assignment syntax.
    def __iter__(self) -> Iterator[AutoName]:

        # NOTE 1: I call 'type(self)' to warranty that it
        # method works even in a subclass of this.
        return (type(self)() for _ in range(self.__count))

    # Search the assigned name of the current object.
    def _search_name(self, frame: Optional[FrameType]) -> str:

        # NOTE 2: The same object could have many names in differents scopes.
        # So, I stores all names in the 'scopes' var. The valid name is one
        # that is in the last scope.
        scopes = []
        m_seen: Set[ModuleType] = {namemodule}  # modules seen
        t_seen: Set[type] = {AutoName}  # types seen

        for variables in _get_outer_locals(frame):

            # NOTE 3: An object could have various names in the same scope. So,
            # I stores all in the 'names' var. This situation happen when user
            # assign the object to multiples variables with the "multiple
            # assignment syntax".
            names: List[str] = []
            variables_items = iter(variables.items())
            for name, value in variables_items:
                len_names = self._search_recursively(
                    value, names, name, m_seen, t_seen)

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
        m_seen: Set[ModuleType],
        t_seen: Set[type],
    ) -> int:
        # search the name in the frame
        if value is self:
            names.append(name)

        # Search the name in a namespace
        elif isinstance(value, type):
            if value not in t_seen:
                t_seen.add(value)
                dir_value = iter(dir(value))
                for attr in dir_value:
                    if getattr(value, attr, None) is self:
                        names.append(attr)
                        break

                # See NOTE 4
                try:
                    attr = next(dir_value)
                except StopIteration:
                    pass
                else:
                    if getattr(value, attr, None) is self:
                        names.append(attr)

        # Search the name in a module
        elif isinstance(value, ModuleType):
            if hasattr(value, "__file__"):
                if value.__file__:
                    if value.__file__ not in _modules_with_autoname_instances \
                    or value in m_seen:  # noqa
                        return len(names)

                m_seen.add(value)
                for key in dir(value):
                    len_names = self._search_recursively(
                        getattr(value, key), names, key, m_seen, t_seen)
                    if len_names > 1:
                        break
        return len(names)

    @property
    def __assigned_name__(self) -> str:
        """Search the name of the instance of the current class."""
        if self.__name is None:
            frame: Optional[FrameType] = inspect.currentframe()
            if frame is None:
                raise _NOT_FOUND_EXCEPTION
            else:
                self.__name = self._search_name(frame.f_back)
        return self.__name
