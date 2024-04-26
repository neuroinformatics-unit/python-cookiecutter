# cookiecutter-python

A tool to automatically create a Python project structure ready to release via GitHub and [PyPI](https://pypi.org/).
It will also set up:
* A blank `README.md` file
* A `LICENSE` file
* [Pre-commit hooks](https://pre-commit.com/) to automate linting checks and formatting
* Automatic versioning using [setuptools_scm](https://github.com/pypa/setuptools_scm)
* A structure for automated tests using [pytest](https://docs.pytest.org/en/7.0.x/)
* Automated formatting checks, testing and release using [GitHub actions](https://github.com/features/actions)
* Documentation using [Sphinx](https://www.sphinx-doc.org/en/master/)

**Based on [cookiecutter-napari-plugin](https://github.com/napari/cookiecutter-napari-plugin)**

## Table of contents
- [Table of contents](#table-of-contents)
- [Set up](#set-up)
	- [Installing Cookiecutter](#installing-cookiecutter)
	- [Creating a Cookiecutter project](#creating-a-cookiecutter-project)
	- [Make it a git repo](#make-it-a-git-repo)
- [Add your modules and tests](#add-your-modules-and-tests)
	- [Add dependencies](#add-dependencies)
	- [Write tests](#write-tests)
- [Before committing your changes](#before-committing-your-changes)
	- [Run the tests](#run-the-tests)
	- [Install your package locally](#install-your-package-locally)
	- [Pre-commit hooks](#pre-commit-hooks)
- [Versioning](#versioning)
	- [Automated versioning](#automated-versioning)
- [GitHub actions workflow](#github-actions-workflow)
- [Documentation](#documentation)
	- [Building the documentation locally](#building-the-documentation-locally)
	- [Publishing the documentation](#publishing-the-documentation)
	- [Docstrings and API documentation](#docstrings-and-api-documentation)

## Set up

### Installing Cookiecutter

First, install cookiecutter in your desired environment. Running in the terminal in your environment, with Pip:

`pip install cookiecutter`

or conda:

`conda install -c conda-forge cookiecutter`

### Creating a Cookiecutter project

In the folder, you want to create the repo run:
```bash
cookiecutter https://github.com/neuroinformatics-unit/python-cookiecutter
```

You will be then asked a series of questions about how you want to set up your project.

For each one, type your answer, enter a single number (or just hit return) to choose from a default option.

* `full_name [Python developer]:` - e.g. `Adam Tyson`
* `email [yourname@example.com]:` - e.g. `cookiecutter@adamltyson.com`
* `github_username_or_organization [githubuser]:` - e.g. `adamltyson`
* `package_name [python-package]:` - e.g. `my-awesome-software`
* `Select github_repository_url:` - Default will be e.g. `https://github.com/adamltyson/my-awesome-software`, but you can also provide this later.
* `module_name [my_awesome_software]:` - The default will be the same as `package_name` but with hyphens converted to underscores.
* `short_description [A simple Python package]:` - Enter a simple, one-line description of your Python package.
* `Select license:` - choose from:
  - `1 - BSD-3`
  - `2 - MIT`
  - `3 - Mozilla Public License 2.0`
  - `4 - Apache Software License 2.0`
  - `5 - GNU LGPL v3.0`
  - `6 - GNU GPL v3.0`
* `Select create_docs:` - Whether to generate documentation using [Sphinx](https://www.sphinx-doc.org/en/master/), choose from:
  - `1 - Yes`
  - `2 - No`

This is the structure cookiecutter will create:
```
└── my-awesome-software/
	├── LICENSE
	├── MANIFEST.in
	├── README.md
	├── pyproject.toml
	├── tox.ini
	├── my_awesome_software/
	│	└── __init__.py
	└── tests/
		├── __init__.py
		├── test_integration/
		│	└── __init__.py
		└── test_unit/
				├── __init__.py
				└──  test_placeholder.py
```
A project with this information will then be written to the current working directory.

If you respond positively to `Select create_docs:`, an additional `docs` folder will be created and two example Python modules (`math.py` and `greetings.py`) will be added to the above structure.
```
└── my-awesome-software/
	└── docs/
		├── make.bat
		├── Makefile
		├── requirements.txt
	    └── source/
			├── api_index.rst
			├── conf.py
			├── getting_started.md
			└── index.rst
	└── my_awesome_software/
		├── __init__.py
		├── greetings.py
		└── math.py
```

### Make it a git repo

Although it asks for a GitHub username or organization and package name, it does not initialize a git repository.

To do so navigate to your project folder:
```bash
cd my-awesome-software
```
and run:
```shell
git init -b main
```

**N.B. If you have an older version of Git (<v2.28), this will produce an error and you will need to run the following:**
```
git init
git checkout -b main
```

Then stage and commit your changes:
```bash
git add .
git commit -m "Initial commit"
```

On GitHub create a new empty repository, and locally add the remote origin and push:
```bash
git remote add origin git@github.com:adamltyson/my-awesome-software.git
git push
```

## Add your modules and tests

Your methods and classes would live inside the folder `my_awesome_software`. Split the functionalities into modules, and save them as `.py` files, e.g.:
```
my_awesome_software
	├── __init__.py
	├── greetings.py
	└── math.py
```

If you want to import methods and classes from one module to another you can use the dot:
```python
# filename: greetings.py
from .math import subtract_two_integers
```

If you want to import all the modules when installing you can add the following to your `__init__.py`:
```python
from . import *
```

### Add dependencies
To ensure any dependencies are installed at the same time as installing
your package, add them to your `pyproject.toml` file. E.g. to add `numpy`
and `pandas` as dependencies, add them to the `dependencies = []` list under
the `[project]` heading:

```toml
dependencies = ["numpy", "pandas"]
```

### Write tests

Write your test methods and classes in the `test` folder. We are using [pytest](https://docs.pytest.org/en/7.2.x/getting-started.html).
In your test module you can call your methods in a simple way:
```python
# filename: test_math.py
from my_awesome_software import math

# here your test function
```

If you're testing a small piece of code, make it a unit test. If you want to test whether two or more software units work well together, create an integration test.

## Before committing your changes

### Run the tests

Be sure that you have installed pytest and run it
```bash
pip install pytest
pytest
```
You should also see coverage information.

### Install your package locally

For a local, editable install, in the project directory, run:
```bash
pip install -e .
```

For a local, editable install with all the development tools (e.g. testing, formatting etc.) run:
```bash
pip install -e '.[dev]'
```

You might want to install your package in an _ad hoc_ environment.

To test if the installation works, try to call your modules with python in another folder from the same environment.
```python
from my_awesome_sofware.math import add_two_integers
add_two_integers(1, 2)
```

### Pre-commit hooks

Running `pre-commit install` will set up [pre-commit hooks](https://pre-commit.com/) to ensure the code is
formatted correctly. Currently, these are:
* [ruff](https://github.com/charliermarsh/ruff) does a number of jobs, including linting, auto-formatting code (with `ruff-format`), and sorting import statements.
* [mypy](https://mypy.readthedocs.io/en/stable/index.html) a static type checker
* [check-manifest](https://github.com/mgedmin/check-manifest) to ensure that the right files are included in the pip package.
* [codespell](https://github.com/codespell-project/codespell) to check for common misspellings.


These will prevent code from being committed if any of these hooks fail. To run them individually:
```bash
ruff check --fix   # Lint all files in the current directory, and fix any fixable errors.
ruff format		   # Format all files in the current directory.
mypy -p my_awesome_software
check-manifest
codespell
```

You can also execute all the hooks using `pre-commit run`. The best time to run this is after you have staged your changes, but before you commit them.

In the case you see `mypy` failing with an error like `Library stubs not installed for this-package`, you do have to edit the `.pre-commit-config.yaml` file by adding the additional dependency to `mypy`:
```yml
- id: mypy
	additional_dependencies:
		- types-setuptools
		- types-this-package
```

## Versioning
We recommend the use of [semantic versioning](https://semver.org/), which uses a `MAJOR`.`MINOR`.`PATCH` versiong number where these mean:

* PATCH = small bugfix
* MINOR = new feature
* MAJOR = breaking change

### Automated versioning
[`setuptools_scm`](https://github.com/pypa/setuptools_scm) can be used to automatically version your package. It has been pre-configured in the `pyproject.toml` file. [`setuptools_scm` will automatically infer the version using git](https://github.com/pypa/setuptools_scm#default-versioning-scheme). To manually set a new semantic version, create a tag and make sure the tag is pushed to GitHub. Make sure you commit any changes you wish to be included in this version. E.g. to bump the version to `1.0.0`:

```bash
git add .
git commit -m "Add new changes"
git tag -a v1.0.0 -m "Bump to version 1.0.0"
git push --follow-tags
```

**N.B. It is also possible to perform this step by using the [GitHub web interface or CLI](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).**


## GitHub actions workflow

A GitHub actions workflow (`.github/workflows/test_and_deploy.yml`) has been set up to run (on each commit/PR):
* Linting checks (pre-commit).
* Testing (only if linting checks pass)
* Release to PyPI (only if a git tag is present and if tests pass). Requires `TWINE_API_KEY` from PyPI to be set in repository secrets.

## Documentation

Software documentation is important for effectively communicating how to use the software to others as well as to your future self.

If you want to include documentation in your package, make sure to respond with `1 - Yes` when prompted during the `cookiecutter` setup. This will instantiate a `docs` folder with a skeleton documentation system, that you can build upon.

The documentation source files are located in the `docs/source` folder and should be written in either [reStructuredText](https://docutils.sourceforge.io/rst.html) or [markdown](https://myst-parser.readthedocs.io/en/stable/syntax/typography.html). The `index.rst` file corresponds to the main page of the documentation website. Other `.rst`  or `.md` files can be included in the main page via the `toctree` directive.

The documentation is built using [Sphinx](https://www.sphinx-doc.org/en/master/) and the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/). The `docs/source/conf.py` file contains the `Sphinx` configuration.

### Building the documentation locally
You can build and view the documentation website locally, on your machine. To do so, run the following commands from the root of your project:
```sh
# Install the documentation build dependencies
pip install -r docs/requirements.txt
# Build the documentation
sphinx-build docs/source docs/build
```
This should create a `docs/build` folder. You can view the local build by opening `docs/build/index.html` in a browser.
To refresh the documentation, after making changes, remove the `docs/build` folder and re-run the above command:

```sh
rm -rf docs/build
sphinx-build docs/source docs/build
```

### Publishing the documentation
We have included an extra GitHub actions workflow in `.github/workflows/docs_build_and_deploy.yml` that will build the documentation and deploy it to [GitHub pages](https://pages.github.com/).
* The build step is triggered every time a pull request is opened or a push is made to the `main` branch. This way you can make sure that the documentation does not break before merging your changes.
* The deployment is triggered only when a tag is present (see [Automated versioning](#automated-versioning)). This ensures that new documentation versions are published in tandem with the release of a new package version on PyPI (see [GitHub actions workflow](#github-actions-workflow)).
* The published docs are by default hosted at `https://<github_username_or_organization>.github.io/<package_name>/`. To enable hosting, you will need to go to the settings of your repository, and under the "Pages" section, select the `gh-pages` branch as the source for your GitHub pages site.
* A popular alternative to GitHub pages for hosting the documentation is [Read the Docs](https://readthedocs.org/). To enable hosting on Read the Docs, you will need to create an account on the website and follow the instructions to link your GitHub repository to your Read the Docs account.

### Docstrings and API documentation
The journey towards good documentation starts with writing docstrings for all functions in your module code. In the example `math.py` and `greetings.py` modules you will find some docstrings that you can use as a template. We have written the example docstrings following the [numpy style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html) but you may also choose another widely used style, such as the [Google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

Once you have written docstrings for all your functions, API documentation can be automatically generated via the [Sphinx autodoc extension](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html). We have given examples of how to do this in the `docs/source/api_index.rst` file.
