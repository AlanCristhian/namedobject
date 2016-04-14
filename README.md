# named

Objects with the `__name__` attribute. E.g:

```python
>>> import named
>>> a = named.Object()
>>> a.__name__
'a'
```

Work with the unpack sintax. E.g:

```python
>>> import named
>>> a, b = named.Object(), named.Object()
>>> a.__name__
'a'
>>> b.__name__
'b'
```

You can use a shorter syntax:

```python
>>> import named
>>> a, b, c = named.Object()*3
>>> a
a
>>> b
b
>>> c
c
```

Don't work with multiple assignment. E.g:

```python
>>> import named
>>> a = b = named.Object()
>>> a.__name__
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.__name__
    ...
NotImplementedError: Can not assing a unique name to multiple variables.
>>> b.__name__
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.__name__
    ...
NotImplementedError: Can not assing a unique name to multiple variables.
```

Note that the error is raised only wen you get the `__name__` attribute.

To make your own subclass that inherit from named.Object, you must chall the
__init__ method.

```python
>>> import named
>>> class Child(named.Object):
...     def __init__(self, arg):
...         super().__init__()
...         self.arg = arg
...
>>> a = Child(1000000)
>>> a.__name__
"a"
>>> a.arg
1000000
```

Also, multiple inheritance is allowed.

```python
>>> import named
... class Numeric:
...     def __init__(self, type):
...         self.__type__ = type
...
>>> class Symbol(Numeric, named.Object):
...     def __init__(self, type):
...         Numeric.__init__(self, type)
...         named.Object.__init__(self)
...
>>> x = Symbol(complex)
>>> x.__name__
"x"
>>> x.__type__
<class 'complex'>
```

**Warning:** See how I initialize bot `Numeric` and `named.Object` base clases.
