---
hide-sidebar: true
---

# python-cookiecutter

A tool to automatically create a Python project structure ready to
release via GitHub and [PyPI](https://pypi.org/).

## Getting Started

**Python-cookiecutter** automatically creates a structured project and sets up essential
tools, including:

-   A blank `README.md` file for documentation.
-   A `LICENSE` file to define usage rights.
-   [Pre-commit hooks](https://pre-commit.com/) to maintain code
    quality.
-   Automatic versioning with
    [setuptools_scm](https://setuptools-scm.readthedocs.io/en/latest/).
-   A test setup using [pytest](https://docs.pytest.org/en/7.0.x/).
-   Automated formatting, testing, and publishing via [GitHub
    Actions](https://github.com/features/actions).
-   A documentation setup with
    [Sphinx](https://www.sphinx-doc.org/en/master/).


::::{grid} 1 2 2 3
:gutter: 3
:class-container: sd-p-3

:::{grid-item-card} {fas}`tools;sd-text-primary` Project Setup
:link: project_setup
:link-type: doc
:text-align: center

Installation and Setup
:::

:::{grid-item-card} {fas}`book-open;sd-text-primary` Infrastructure
:link: infrastructure
:link-type: doc
:text-align: center

Pre-commit hooks, Versioning, GitHub Actions & Documentation
:::

:::{grid-item-card} {fas}`handshake-angle;sd-text-primary` Contributing
:link: contributing
:link-type: doc
:text-align: center

How to improve the cookiecutter
:::
::::


```{toctree}
:maxdepth: 2
:caption: Documentation
:hidden:

project_setup
infrastructure
contributing
```
