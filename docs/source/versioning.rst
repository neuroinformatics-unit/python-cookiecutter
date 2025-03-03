Versioning
==========

We recommend following [Semantic Versioning](https://semver.org/) where versions follow a ``MAJOR.MINOR.PATCH`` scheme:

- **PATCH**: Bug fixes.
- **MINOR**: New features.
- **MAJOR**: Breaking changes.

Automated Versioning
--------------------

The project is configured to use ``setuptools_scm`` to automatically determine the version based on Git tags.
To release a new version, commit your changes and create a new tag. For example, to bump to version ``1.0.0``:

.. code-block:: bash

   git add .
   git commit -m "Add new changes"
   git tag -a v1.0.0 -m "Bump to version 1.0.0"
   git push --follow-tags

You can also use the GitHub interface or CLI to create tags.
