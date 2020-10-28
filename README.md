# name

A library with a base class that stores the assigned name of an object.

```pycon
>>> import name
>>> x, y = name.AutoName()
>>> x.__name__
'x'
>>> y.__name__
'y'
```

## Table Of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Tutorial](#tutorial)
- [Observations](#observations)
    - [How it works](#how-it-works)
    - [Multiple assignment syntax](#multiple-assygnment)
- [API reference](#api-refernce)
    - [class AutoName()](#class-auto)

## Requirements <a name="requirements"></a>

`name` requires Python 3.6 or newer. It has no third-party dependencies and
works on both POSIX and Windows.

## Installation <a name="installation"></a>

```shell
$ pip install git+https://github.com/AlanCristhian/name.git
```

## Tutorial <a name="tutorial"></a>

`name` has only one class: `AutoName`. It creates an object with the
`__name__` attribute that stores the name of such object. E.g:

```pycon
>>> import name
>>> a = name.AutoName()
>>> a.__name__
'a'
```

It can make multiple variables with iterable unpacking syntax.

```pycon
>>> import name
>>> x, y = name.AutoName()
>>> x.__name__
'x'
>>> y.__name__
'y'
```

`AutoName` is also a *context manager* that you can use in a `with` statement.

```pycon
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
```

You can make your own subclass that inherit from `name.AutoName`.

```pycon
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
```

## Observations <a name="observations"></a>

### How it works <a name="how-it-works"></a>

`AutoName` searches the name of the object in the bytecode of the frame where
the object was created. If it can't find a name, then the default
`'<nameless>'` value are set.

### Multiple assignment syntax <a name="multiple-assygnment"></a>

`AutoName` stores the last name in the expression.

```pycon
>>> import name
>>> a = b = name.AutoName()
>>> a.__name__
'b'
>>> b.__name__
'b'
```

That is the same behaviour of `__set_name__` method.

```pycon
>>> class SetName:
...     def __set_name__(self, owner, name):
...         self.__name__ = name
...
>>> class MyClass:
...     a = b = SetName()
...
>>> MyClass.a.__name__
'b'
>>> MyClass.b.__name__
'b'
```

## API reference <a name="api-refernce"></a>

### class AutoName() <a name="class-auto"></a>

Stores the assigned name of an object in the `__name__` attribute.

Single assignment:

```pycon
>>> obj = AutoName()
>>> obj.__name__
'obj'
```

Iterable unpacking syntax:

```pycon
>>> a, b = AutoName()
>>> a.__name__
'a'
>>> b.__name__
'b'
```

Context manager:

```pycon
>>> with AutoName() as (e, f):
...     (e.__name__, f.__name__)
...
('e', 'f')
```
