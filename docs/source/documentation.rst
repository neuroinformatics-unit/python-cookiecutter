Documentation
=============

Good documentation is key for both users and developers. If you chose to create docs during cookiecutter setup,
a ``docs`` folder was generated with a basic Sphinx configuration.

Building the Documentation Locally
----------------------------------

To build the docs locally:

1. Install the build requirements:

   .. code-block:: bash

      pip install -r docs/requirements.txt

2. Build the documentation:

   .. code-block:: bash

      sphinx-build docs/source docs/build

Open ``docs/build/index.html`` in your browser to view the docs.

Refreshing the Build
--------------------

After updating your documentation, remove the build folder and rebuild:

.. code-block:: bash

   rm -rf docs/build
   sphinx-build docs/source docs/build

Publishing the Documentation
----------------------------

A separate GitHub Actions workflow (``.github/workflows/docs_build_and_deploy.yml``) builds and deploys
the documentation to GitHub Pages when changes are pushed to ``main`` or when a tag is created.

Docstrings and API Documentation
--------------------------------

Write clear docstrings for all functions in your code (e.g. using the NumPy or Google style).
Sphinx’s ``autodoc`` extension automatically generates API documentation from these docstrings.
For an example setup, see the ``docs/source/api_index.rst`` file.
