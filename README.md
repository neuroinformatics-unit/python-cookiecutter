# cookiecutter-python

A tool to automatically create a Python project structure ready to release via GitHub and [PyPI](https://pypi.org/).
It will also set up:
* A blank `README.md` file
* A `LICENSE` file
* Formatting checks using [flake8](https://flake8.pycqa.org/en/latest/)
* Autoformatting using [Black](https://black.readthedocs.io/en/stable/) 
* [Pre-commit hooks](https://pre-commit.com/)
* Automatic versioning using [bump2version](https://github.com/c4urself/bump2version)
* A structure for automated tests using [pytest](https://docs.pytest.org/en/7.0.x/)
* Automated formatting checks, testing and release using [GitHub actions](https://github.com/features/actions)

**Based on [cookiecutter-napari-plugin](https://github.com/napari/cookiecutter-napari-plugin)**

## Set up

First, install cookiecutter in your desired environment.

In the folder, you want to create the repo run:
```bash
cookiecutter https://github.com/SainsburyWellcomeCentre/python-cookiecutter
```

You will be then asked a series of questions about how you want to set up your project.

For each one, type your answer, enter a single number (or just hit return) to choose from a default option.

* `full_name [Python developer]:` - e.g. `Adam Tyson`
* `email [yourname@example.com]:` - e.g. `cookiecutter@adamltyson.com`
* `github_username_or_organization [githubuser]: ` - e.g. `adamltyson`
* `package_name [python-package]:` - e.g. `my-awesome-software`
* `Select github_repository_url:` - Default will be e.g. `https://github.com/adamltyson/my-awesome-software`, but you can also provide this later.
* `module_name [my_awesome_software]:` - The default will be the same as `package_name` but with hyphens converted to underscores.
* `short_description [A simple Python package]` - Enter a simple, one-line description of your Python package. 
* `Select license:` - choose from:
  - `1 - BSD-3`
  - `2 - MIT`
  - `3 - Mozilla Public License 2.0`
  - `4 - Apache Software License 2.0`
  - `5 - GNU LGPL v3.0`
  - `6 - GNU GPL v3.0`

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

### Make it a git repo

Although it asks for a GitHub username or organization and package name, it does not initialize a git repository.

To do so navigate to your project folder:
```bash
cd my-awesome-software`
```
and run:
```shell
git init -b main
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

Your methods and classes would live inside the folder `my_awesome_software`. Split the functionalities into modules, and save them as `.py` files.
```
my_awesome_software
	├── __init__.py
	├── math.py
	├── more_math.py
```

If you want to import methods and classes from one module to another you can use the dot:
```python
# filename: maths.py
from .more_math import subtract
```

If you want to import all the modules when installing you can add the following to your `__init__.py`:
```python
from . import *
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
from my_awesome_sofware.maths import add_numbers
add_numbers(1, 2)
```

### Pre-commit hooks

Running `pre-commit install` will run set up [pre-commit hooks](https://pre-commit.com/) to ensure the code is 
formatted correctly. Currently, these are:
* [black](https://black.readthedocs.io/en/stable/) for code structure formatting (maximum line length set to 79)
* [flake8](https://flake8.pycqa.org/en/latest/) to enforce [PEP8](https://www.python.org/dev/peps/pep-0008/)
* [mypy](https://mypy.readthedocs.io/en/stable/index.html) a static type checker
* [isort](https://pycqa.github.io/isort/) sorts imports alphabetically

These will prevent code from being committed if any of these hooks fail. To run them individually:
```bash
black ./
flake8
mypy
isort
```

You can also run `pre-commit` to run all of them before trying to commit.

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
[`setuptools_scm`](https://github.com/pypa/setuptools_scm) can be used to automatically version your package. It has been pre-configured in the `pyproject.toml` file. [`setuptools_scm` will automatically infer the version using git](https://github.com/pypa/setuptools_scm#default-versioning-scheme). To manually set a new semantic version, create a tag and make sure the tag is pushed to GitHub. E.g. to bump the version to `1.0.0`:

```bash
git tag -a v1.0.0 -m "Bump to version 1.0.0"
git push --follow-tags
```


## GitHub actions workflow

A GitHub actions workflow (`.github/workflows/test_and_deploy.yml`) has been set up to run (on each commit/PR):
* Linting checks (pre-commit).
* Testing (only if linting checks pass)
* Release to PyPI (only if a git tag is present and if tests pass). Requires `TWINE_API_KEY` from PyPI to be set in repository secrets.

