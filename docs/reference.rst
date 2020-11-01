API reference
-------------

.. py:class:: AutoName()

    Stores the assigned name of an object in the ``name`` attribute.

    Single assignment: ::

        >>> obj = AutoName()
        >>> obj.name
        'obj'

    Iterable unpacking syntax: ::

        >>> a, b = AutoName()
        >>> a.name
        'a'
        >>> b.name
        'b'
