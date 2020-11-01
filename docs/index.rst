.. objname documentation master file, created by
   sphinx-quickstart on Sat Oct 10 19:33:22 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to objname's documentation!
===================================

``objname`` is a library with a base class that stores the assigned name of an
object::

    >>> import objname
    >>> x, y = objname.AutoName()
    >>> x.name
    'x'
    >>> y.name
    'y'

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   requirements
   installation
   tutorial
   reference
   observations
   contribute
   donation
   license
