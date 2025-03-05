# Neuroinformatics Unit Python cookiecutter

The Neuroinformatics Unit (NIU) is a **Research Software Engineering** team based at the **Sainsbury Wellcome Centre** and the **Gatsby Computational Neuroscience Unit**.

The NIU is dedicated to the development of high quality, accurate, robust, easy to use and maintainable open-source software for neuroscience and machine learning. We collaborate with researchers and other software engineers to advance research in the two research centres and make new algorithms and tools available to the global community,[Read more](https://neuroinformatics.dev/index.html).

## Python cookiecutter

A tool to automatically create a Python project structure ready to
release via GitHub and [PyPI](https://pypi.org/).

### Getting Started

**Python-cookiecutter** is a tool that helps you quickly set up a Python
project with everything needed to publish it in a very easy steps on GitHub and
[PyPI](https://pypi.org/).

It automatically creates a structured project and sets up essential
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

This tool is based on
[cookiecutter-napari-plugin](https://github.com/napari/napari-plugin-template)
and provides a solid starting point for your projects.

>With this tool, you can start immediately without manually setting up
everything!


```{toctree}
:maxdepth: 2
:caption: Documentation
:hidden:

project_setup
modules
github_actions_setup
pre_commits
versioning
documentation
contributing
```
