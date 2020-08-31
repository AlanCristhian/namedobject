====
name
====

A library with a base class that stores the assigned name of an object. ::

  >>> import name
  >>> x, y = name.AutoName()
  >>> x.__name__
  'x'
  >>> y.__name__
  'y'

------------
Requirements
------------

`name` requires Python 3.6 or newer. It has no third-party dependencies and
works on both POSIX and Windows.

------------
Installation
------------

  `$ pip install git+https://github.com/AlanCristhian/name.git`

--------
Tutorial
--------

`name` has only one class: `AutoName`. It creates an object with the
`__name__` attribute that stores the name of such object. E.g: ::

  >>> import name
  >>> a = name.AutoName()
  >>> a.__name__
  'a'

It can make multiple variables using the unpack sequence syntax: ::

  >>> import name
  >>> x, y = name.AutoName()
  >>> x.__name__
  'x'
  >>> y.__name__
  'y'

`AutoName` can create as many variables as you want with the iterable
unpacking syntax. It will always know how many variables to create and what
name to assign each one.

  >>> import name
  >>> a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s = name.AutoName()
  >>> k.__name__
  'k'

It works with the *for loop*:

  >>> for x, y, z in [name.AutoName()]:
  ...     (x.__name__, y.__name__, z.__name__)
  ...
  ('x', 'y', 'z')

You can make your own subclass that inherit from `name.AutoName`. ::

  >>> import name
  >>> class Number(name.AutoName):
  ...     def __init__(self, value):
  ...         super().__init__()
  ...         self.value = value
  ...
  >>> a = Number(1)
  >>> a.__name__
  "a"
  >>> a.value
  1

Also works with multiple inheritance. ::

  >>> import name
  ... class Numeric:
  ...     def __init__(self, type):
  ...         self.type = type
  ...
  >>> class Symbol(Numeric, name.AutoName):
  ...     def __init__(self, type):
  ...         Numeric.__init__(self, type)
  ...         name.AutoName.__init__(self)
  ...
  >>> c = Symbol(complex)
  >>> c.__name__
  'c'
  >>> c.type
  <class 'complex'>

**Note:** See how both `Numeric` and `name.AutoName` have been initialized.

`AutoName` is also a *context manager* that you can use in a
`with` statement. ::

  >>> import name
  >>> with name.AutoName() as obj:
  ...     obj.__name__
  ...
  'obj'
  >>> with name.AutoName() as (x, y, z):
  ...     (x.__name__, y.__name__, z.__name__)
  ...
  ('x', 'y', 'z')
  >>>

------------
How it works
------------

`AutoName` searches the name of the object in the bytecode of the frame where
the object was created. If it can't find, searches it in the upper frame an so
until the object name is found. I it can't find a name, then the default
`'<nameless>'` value are set.

-------
Caveats
-------

Multiple assignment syntax
==========================

`AutoName` stores the last name in the expression in the same way that
`__set_name__` does. ::

  >>> import name
  >>> a = b = name.AutoName()
  >>> a.__name__
  'a'
  >>> b.__name__
  'b'

`See the \_\_set_name\_\_ documentation<https://docs.python.org/3/reference/datamodel.html?highlight=__get__#object.__set_name__>`

AutoName instance as attribute of an object
===========================================

You can't create an instance of `AutoName` and store it in an object
attibute: ::

  >>> import name
  >>> class Object:
  ...     def __init__(self):
  ...         self.attribute = name.AutoName()
  ...
  >>> Object().attribute.__name__
 '<nameless>'

**To do that** the attribute should be an *class attribute*: ::

  >>> import name
  >>> class Object:
  ...     attribute = name.AutoName()
  ...     def __init__(self):
  ...         ...
  ...
  >>> Object().attribute.__name__
  'attribute'
