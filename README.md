
[![Project chat](https://img.shields.io/badge/zulip-join_chat-brightgreen.svg)](https://neuroinformatics.zulipchat.com/#narrow/channel/406003-Python-cookiecutter)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-orange.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/format.json)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# python-cookiecutter

A tool to automatically create a Python project structure ready to release via GitHub and [PyPI](https://pypi.org/).

**python-cookiecutter** automatically creates a structured project and sets up essential
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

## Quick Install

First, install cookiecutter in your desired environment. Running in the terminal in your environment, with Pip:

```sh
pip install cookiecutter

# or conda:

conda install -c conda-forge cookiecutter
```
### Creating a Cookiecutter project

In the folder, you want to create the repo run:

```sh
cookiecutter https://github.com/neuroinformatics-unit/python-cookiecutter
```
You will be then asked a series of questions about how you want to set up your project.

[View Full Documentation →](python-cookiecutter.neuroinformatics.dev)

## Contributing

We welcome contributions! See our [Contribution Guidelines](python-cookiecutter.neuroinformatics.dev/contributing) for workflow details.

## License
⚖️ [BSD 3-Clause](./LICENSE)
