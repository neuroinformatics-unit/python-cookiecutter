Getting Started
===============

**python-cookiecutter** is a tool that helps you quickly set up a Python project with everything needed to publish it on GitHub and `PyPI <https://pypi.org/>`_.

It automatically creates a structured project and sets up essential tools, including:

- A blank ``README.md`` file for documentation.
- A ``LICENSE`` file to define usage rights.
- `Pre-commit hooks <https://pre-commit.com/>`_ to maintain code quality.
- Automatic versioning with `setuptools_scm <https://github.com/pypa/setuptools_scm>`_.
- A test setup using `pytest <https://docs.pytest.org/en/7.0.x/>`_.
- Automated formatting, testing, and publishing via `GitHub Actions <https://github.com/features/actions>`_.
- A documentation setup with `Sphinx <https://www.sphinx-doc.org/en/master/>`_.

This tool is based on `cookiecutter-napari-plugin <https://github.com/napari/cookiecutter-napari-plugin>`_ and provides a solid starting point for your projects.

Features
--------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - :octicon:`package` **Project Setup**
     - Pre-configured ``pyproject.toml``, ``LICENSE``, and test folder.
   * - :octicon:`workflow` **CI/CD**
     - Automated testing and deployment using GitHub Actions.
   * - :octicon:`book` **Documentation**
     - Sphinx setup with PyData theme and auto API generation.

With this tool, you can start  immediately without manually setting up everything! 🚀
