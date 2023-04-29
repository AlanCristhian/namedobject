# objname

A library with a base class that stores the assigned name of an object.

```pycon
>>> import objname
>>> x, y = objname.AutoName()
>>> x.name
'x'
>>> y.name
'y'
```

Official documentation at readthedocs: https://objname.readthedocs.io/en/latest/

## Table Of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Tutorial](#tutorial)
- [Observations](#observations)
    - [How it works](#how-it-works)
    - [Multiple assignment syntax](#multiple-assygnment)
- [API reference](#api-refernce)
    - [class AutoName()](#class-auto)
    - [class AutoNameAttr(attr: str)](#class-autonameattr)
- [Contribute](#contribute)
- [Donation](#donation)
- [License](#license)

## Requirements <a name="requirements"></a>

`objname` requires Python 3.6 or newer. It has no third-party dependencies and
works on both POSIX and Windows. It runs in cPython and PyPy.

## Installation <a name="installation"></a>

To install it just use ``pip``:

```shell
$ pip install objname
```

You can also install it from *github*:

```shell
$ pip install git+https://github.com/AlanCristhian/objname.git
```

## Tutorial <a name="tutorial"></a>

`objname` has only one class: `AutoName`. It creates an object with the
`objname` attribute that stores the name of such object. E.g:

```pycon
>>> import objname
>>> a = objname.AutoName()
>>> a.name
'a'
```

It can make multiple variables with iterable unpacking syntax.

```pycon
>>> import objname
>>> x, y = objname.AutoName()
>>> x.name
'x'
>>> y.name
'y'
```

You can make your own subclass that inherit from `objname.AutoName`.

```pycon
>>> import objname
>>> class Number(objname.AutoName):
...     def __init__(self, value):
...         super().__init__()
...         self.value = value
...
>>> a = Number(1)
>>> a.name
'a'
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
>>> import objname
>>> a = b = objname.AutoName()
>>> a.name
'b'
>>> b.name
'b'
```

That is the same behaviour of `__set_name__` method.

```pycon
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
```

### The AutoNameAttr class

The `AutoNameAttr` metaclass creates a class that assign the name to an
user defined attribute. For example, you want to assign the name to the
`__name__` attribute instead of `.name`.

```pycon
>>> AutoName__name__ = AutoNameAttr("__name__")
>>> class MyClass(AutoName__name__):
...     pass
...
>>> my_obj = MyClass()
>>> my_obj.__name__
'my_obj'
>>> my_obj.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyClass' object has no attribute 'name'
```

As you can see, it only assign the name to the choosen attribute.

## API reference <a name="api-refernce"></a>

### class AutoName() <a name="class-auto"></a>

Stores the assigned name of an object in the `name` attribute.

Single assignment:

```pycon
>>> obj = AutoName()
>>> obj.name
'obj'
```

Iterable unpacking syntax:

```pycon
>>> a, b = AutoName()
>>> a.name
'a'
>>> b.name
'b'
```

### class:: AutoNameAttr(attr: str) <a name="class-autonameattr"></a>

Creates a class that stores the assigned name of an object in the ``attr``
attribute.

Example, you want to store the object name in the ``__name__`` attribute:

```pycon
>>> AutoName__name__ = AutoNameAttr("__name__")
>>> class MyClass(AutoName__name__):
...     pass
...
>>> my_obj = MyClass()
>>> my_obj.__name__
'my_obj'
>>> my_obj.name
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'MyClass' object has no attribute 'name'
```

## Contribute <a name="contribute"></a>

- Issue Tracker: https://github.com/AlanCristhian/objname/issues
- Source Code: https://github.com/AlanCristhian/objname

## Donation <a name="donation"></a>

Buy Me a Coffee 🙂: https://www.paypal.com/donate?hosted_button_id=KFJYZEVQVRQDE

## License <a name="license"></a>

The project is licensed under the MIT license.
