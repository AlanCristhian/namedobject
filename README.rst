====
name
====

A library with a base class that stores the assigned name of an object. ::

  >>> import name
  >>> a = name.AutoName()
  >>> a.__assigned_name__
  'a'

------------
Installation
------------

  ``$ pip install git+https://github.com/AlanCristhian/name.git``

--------
Tutorial
--------

This module only have one class: ``AutoName``. This creates an object with the
``__assigned_name__`` attribute that stores the name. E.g: ::

  >>> import name
  >>> a = name.AutoName()
  >>> a.__assigned_name__
  'a'

You can create multiples variables using the unpack sequence syntax. To do that
you must pass the amount of object that you want as argument.::

  >>> import name
  >>> a, b, c = name.AutoName(3)
  >>> a.__assigned_name__
  'a'
  >>> b.__assigned_name__
  'b'
  >>> c.__assigned_name__
  'c'

To make your own subclass that inherit from ``name.AutoName``, you must chall
the ``__init__`` method. ::

  >>> import name
  >>> class Number(name.AutoName):
  ...     def __init__(self, value, count=0):
  ...         super().__init__(count)
  ...         self.value = value
  ...
  >>> a = Number(1)
  >>> a.__assigned_name__
  "a"
  >>> a.value
  1

Also, multiple inheritance is allowed. ::

  >>> import name
  ... class Numeric:
  ...     def __init__(self, type):
  ...         self.type = type
  ...
  >>> class Symbol(Numeric, name.AutoName):
  ...     def __init__(self, type, count=0):
  ...         Numeric.__init__(self, type)
  ...         name.AutoName.__init__(self, count)
  ...
  >>> c = Symbol(complex)
  >>> c.__assigned_name__
  'c'
  >>> c.type
  <class 'complex'>

**Warning:** See how I initialize bot ``Numeric`` and ``name.AutoName``
base clases.

-------
Caveats
-------

Multiple assignment syntax
==========================

They wont work with multiple assignment. E.g: ::


  >>> import name
  >>> a = b = name.AutoName()
  >>> a.__assigned_name__
  Traceback (most recent call last):
    File "<pyshell#2>", line 1, in <module>
      a.__assigned_name__
      ...
  NotImplementedError: Can not assign multiples names to the same object.
  >>> b.__assigned_name__
  Traceback (most recent call last):
    File "<pyshell#2>", line 1, in <module>
      a.__assigned_name__
      ...
  NotImplementedError: Can not assign multiples names to the same object.

Note that the error is raised only wen you get the `__assigned_name__`
attribute.

\_\_assigned_name\_\_ in the body of \_\_init\_\_
=================================================

If you make a subclass of ``AutoName``, you can not access to the
``__assigned_name__`` property from the ``__init__`` method. ::

  >>> import name
  >>> class Number(name.AutoName):
  ...     def __init__(self, count=0):
  ...         super().__init__(count)
  ...         self.name = self.__assigned_name__
  ...
  >>> n = Number()
  >>> n.name
  'self'
  >>> n.__assigned_name__
  'self'

As you can see, the response is wrong. That is because `__assigned_name__` is a
method. They can find the name of the object after the object was created.

**To solve that** make a *getter* method: ::

  >>> import name
  >>> class Number(name.AutoName):
  ...     def __init__(self, count=0):
  ...         super().__init__(count)
  ...     @property
  ...     def name(self):
  ...         return self.__assigned_name__
  ...
  >>> n = Number()
  >>> n.name
  'n'
