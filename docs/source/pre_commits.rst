Before Committing Your Changes
==============================

Ensure that your code passes all tests and follows formatting standards before committing.

Running the Tests
-----------------

Install pytest if needed and run the tests:

.. code-block:: bash

   pip install pytest
   pytest

Local Installation
------------------

For a local, editable install run:

.. code-block:: bash

   pip install -e .

For development (with additional tools):

.. code-block:: bash

   pip install -e '.[dev]'

Testing the Installation
------------------------

Test that your modules work from another folder:

.. code-block:: python

   from my_awesome_software.math import add_two_integers
   add_two_integers(1, 2)

Pre-commit Hooks
----------------

Setting up pre-commit hooks ensures consistent code quality. Install them by running:

.. code-block:: bash

   pre-commit install

The hooks include:
- **ruff**: For linting, formatting, and import sorting.
- **mypy**: For static type checking.
- **check-manifest**: To verify the correct files are packaged.
- **codespell**: To catch common misspellings.

To run all hooks before committing, use:

.. code-block:: bash

   pre-commit run
