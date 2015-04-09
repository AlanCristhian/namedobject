# namedobject

Objects with the `__name__` attribute. E.g:

```python
>>> import namedobject
>>> a = namedobject.NamedObject()
>>> a.__name__
'a'
```

Work with the unpack sintax. E.g:

```python
>>> import namedobject
>>> a, b = namedobject.NamedObject(), namedobject.NamedObject()
>>> a.__name__
'a'
>>> b.__name__
'b'
```

Don't work with multiple assignment. E.g:

```python
>>> import namedobject
>>> a = b = namedobject.NamedObject()
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

Note that the error is showed only wen you get the `__name__` attribute.
