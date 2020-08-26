# name

A library with a base class that stores the assigned name of an object.

```pycon
>>> import name
>>> a = name.AutoName()
>>> a.__name__
'a'
```

## Requirements

`name` requires Python 3.6 or newer. It has no third-party dependencies and
works on both POSIX and Windows.

## Installation

```shell
$ pip install git+https://github.com/AlanCristhian/name.git
```

## Tutorial

`name` has only one class: `AutoName`. It creates an object with the
`__name__` attribute that stores the name. E.g:

```pycon
>>> import name
>>> a = name.AutoName()
>>> a.__name__
'a'
```

It can make multiple variables using the unpack sequence syntax. To do that
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
...     def __init__(self, value, count=1):
...         super().__init__(count)
...         self.value = value
...
>>> a = Number(1)
>>> a.__name__
"a"
>>> a.value
1
```

Also works with multiple inheritance.

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

**Warning:** See how both `Numeric` and `name.AutoName` have been initialized.

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

### How it works

If the object is in `__main__`, `AutoName` searches the name of the object in
the frame where the object was created. If it can't find, searches it in the
upper frame an so until the object name is found. I it can't find a name, then
the default `<nameless>` value are set.

If the object is in a module, just look for its name in the global namespace.

The name will be searched only if you look up the `.__name__` property, not at
the instantiation time. The name is cached once has been found.

### Multiple assignment syntax

`AutoName` stores the last name in the expression in the same way that
`__set__name__` does.

```pycon
>>> import name
>>> a = b = name.AutoName()
>>> a.__name__
'a'
>>> b.__name__
'b'
```
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
