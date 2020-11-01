Tutorial
--------

``name`` has only one class: ``AutoName``. It creates an object with the
``name`` attribute that stores the name of such object. E.g: ::

    >>> import name
    >>> a = name.AutoName()
    >>> a.name
    'a'

It can make multiple variables with iterable unpacking syntax. ::

    >>> import name
    >>> x, y = name.AutoName()
    >>> x.name
    'x'
    >>> y.name
    'y'

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
