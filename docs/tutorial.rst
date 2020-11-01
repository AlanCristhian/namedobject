Tutorial
--------

``objname`` has only one class: ``AutoName``. It creates an object with the
``objname`` attribute that stores the name of such object. E.g: ::

    >>> import objname
    >>> a = objname.AutoName()
    >>> a.name
    'a'

It can make multiple variables with iterable unpacking syntax. ::

    >>> import objname
    >>> x, y = objname.AutoName()
    >>> x.name
    'x'
    >>> y.name
    'y'

You can make your own subclass that inherit from ``objname.AutoName``. ::

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
