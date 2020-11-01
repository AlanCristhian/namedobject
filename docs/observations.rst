Observations
------------

How it works
~~~~~~~~~~~~

``AutoName`` searches the name of the object in the bytecode of the frame where
the object was created. If it can't find a name, then the default
``'<nameless>'`` value are set.

Multiple assignment syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~

``AutoName`` stores the last name in the expression. ::

    >>> import name
    >>> a = b = name.AutoName()
    >>> a.name
    'b'
    >>> b.name
    'b'

That is the same behaviour of ``__set_name__`` method. ::

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
