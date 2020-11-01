name
====

A library with a base class that stores the assigned name of an object. ::

    >>> import name
    >>> x, y = name.AutoName()
    >>> x.name
    'x'
    >>> y.name
    'y'

Official documentation at readthedocs: https://auto-name.readthedocs.io/en/latest/

.. contents:: Table of Contents

Requirements
------------

``name`` requires Python 3.6 or newer. It has no third-party dependencies and
works on both POSIX and Windows. It runs in cPython and PyPy.

Installation
------------

To install it just use ``pip``::

    $ pip install name

You can also install it from *github*::

    $ pip install git+https://github.com/AlanCristhian/name.git

Tutorial
--------

``name`` has only one class: ``AutoName``. It creates an object with the
``__name__`` attribute that stores the name of such object. E.g: ::

    >>> import name
    >>> a = name.AutoName()
    >>> a.name
    'a'

You can make your own subclass that inherit from ``name.AutoName``. ::

    >>> import name
    >>> class Number(name.AutoName):
    ...     def __init__(self, value):
    ...         super().__init__()
    ...         self.value = value
    ...
    >>> a = Number(1)
    >>> a.name
    'a'
    >>> a.value
    1

Observations
------------

How it works
~~~~~~~~~~~~

``AutoName`` searches the name of the object in the bytecode of the frame where
the object was created. If it can't find a name, then the default
``'<nameless>'`` value are set.

Multiple assignment syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~

``AutoName`` stores the last name in the expression. ::

    >>> import name
    >>> a = b = name.AutoName()
    >>> a.name
    'b'
    >>> b.name
    'b'

That is the same behaviour of ``__set_name__`` method. ::

    >>> class SetName:
    ...     def __set_name__(self, owner, name):
    ...         self.name = name
    ...
    >>> class MyClass:
    ...     a = b = SetName()
    ...
    >>> MyClass.a.name
    'b'
    >>> MyClass.b.name
    'b'

API reference
-------------

.. class:: AutoName()

   Stores the assigned name of an object in the ``name`` attribute.

   Single assignment: ::

       >>> obj = AutoName()
       >>> obj.name
       'obj'

   Iterable unpacking syntax: ::

       >>> a, b = AutoName()
       >>> a.name
       'a'
       >>> b.name
       'b'

Contribute
----------

- Issue Tracker: https://github.com/AlanCristhian/name/issues
- Source Code: https://github.com/AlanCristhian/name

Support
-------

If you are having issues, please report it at
`github <https://github.com/AlanCristhian/name/issues>`_

License
-------

The project is licensed under the MIT license.
