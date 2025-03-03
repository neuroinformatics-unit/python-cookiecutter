Modules and Tests
=================

Your Python code should live in the ``my_awesome_software`` package.
You can organize your code into multiple modules and write tests to ensure everything works as expected.

Adding Modules
--------------

Create your Python modules as separate ``.py`` files. For example:

.. code-block:: text

   my_awesome_software/
       ├── __init__.py
       ├── greetings.py
       └── math.py

To import functions between modules, use relative imports:

.. code-block:: python

   # Inside greetings.py
   from .math import subtract_two_integers

If you want to import all modules when installing, add the following in ``__init__.py``:

.. code-block:: python

   from . import *

Adding Dependencies
-------------------

To include dependencies (e.g. ``numpy``, ``pandas``), list them in the ``pyproject.toml`` file:

.. code-block:: toml

   [project]
   dependencies = ["numpy", "pandas"]

Writing Tests
-------------

Place your tests in the ``tests`` directory. Use pytest to write unit tests and integration tests.
For example, a unit test in ``tests/test_unit/test_math.py`` might look like:

.. code-block:: python

   from my_awesome_software import math

   def test_add_two_integers():
       assert math.add_two_integers(1, 2) == 3
