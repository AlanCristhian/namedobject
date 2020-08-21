# name

A library with a base class that stores the assigned name of an object.

```pycon
>>> import name
>>> a = name.AutoName()
>>> a.__name__
'a'
```

## Installation

```shell
$ pip install git+https://github.com/AlanCristhian/name.git
```

## Tutorial

This module only have one class: ``AutoName``. This creates an object with the
`__name__` attribute that stores the name. E.g:

```pycon
>>> import name
>>> a = name.AutoName()
>>> a.__name__
'a'
```

You can create multiples variables using the unpack sequence syntax. To do that
you must pass the amount of object that you want as argument.

```pycon
>>> import name
>>> a, b, c = name.AutoName(3)
>>> a.__name__
'a'
>>> b.__name__
'b'
>>> c.__name__
'c'
```

To make your own subclass that inherit from `name.AutoName`, you must chall
the `__init__` method.

```pycon
>>> import name
>>> class Number(name.AutoName):
...     def __init__(self, value, count=0):
...         super().__init__(count)
...         self.value = value
...
>>> a = Number(1)
>>> a.__name__
"a"
>>> a.value
1
```

Also, multiple inheritance is allowed.

```pycon
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
>>> c.__name__
'c'
>>> c.type
<class 'complex'>
```

**Warning:** See how I initialize both `Numeric` and `name.AutoName`
base clases.

`AutoName` is also a *context manager* that you can use in a `with` statement.

```pycon
>>> import name
>>> with name.AutoName() as obj:
...     obj.__name__
...
'obj'
>>> with name.AutoName(3) as (x, y, z):
...     (x.__name__, y.__name__, z.__name__)
...
('x', 'y', 'z')
>>>
```

## Caveats

### Multiple assignment syntax

They wont work with multiple assignment. E.g:

```pycon
>>> import name
>>> a = b = name.AutoName()
>>> a.__name__
'a'
>>> b.__name__
'b'
```

`AutoName` store the first name in the expression.

### Custom attribute name to store the object name

If you make a subclass of `AutoName`, you can not access to the
`__name__` property from the `__init__` method.

```pycon
>>> import name
>>> class Number(name.AutoName):
...     def __init__(self, count=0):
...         super().__init__(count)
...         self.name = self.__name__
...
>>> n = Number()
>>> n.name
'self'
>>> n.__name__
'self'
```

As you can see, the response is wrong. That is because `__name__` is a
method. They can find the name of the object after the object was created.

**To solve that** make a *getter* method:

```pycon
>>> import name
>>> class Number(name.AutoName):
...     @property
...     def name(self):
...         return self.__name__
...
>>> n = Number()
>>> n.name
'n'
```

### AutoName instance as attribute of an object

You can't create an instance of `AutoName` and store it in an object attibute:

```pycon
>>> import name
>>> class Object:
...     def __init__(self):
...         self.attribute = name.AutoName()
...
>>> Object().attribute.__name__
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
  ...
NameError: The name of this object has not been found.
```

**To do that** the attribute should be an *class attribute*:

```pycon
>>> import name
>>> class Object:
...     attribute = name.AutoName()
...     def __init__(self):
...         ...
...
>>> Object().attribute.__name__
'attribute'
```
