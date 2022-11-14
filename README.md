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

**Based on the [cookiecutter-napari-plugin](https://github.com/napari/cookiecutter-napari-plugin)**

### To set up:

#### First install cookiecutter:
```
pip install cookiecutter
```

#### Then run:

```
cookiecutter https://github.com/SainsburyWellcomeCentre/python-cookiecutter
```

#### Then you will be asked a series of questions about how you want to set up your project

For each one, type your answer, enter a single number (or just hit return) to choose from a default option.

* `full_name [Python developer]:` - e.g. `Adam Tyson`
* `email [yourname@example.com]:` - e.g. `cookiecutter@adamltyson.com`
* `github_username_or_organization [githubuser]: ` - e.g. `adamltyson`
* `package_name [python-package]:` - e.g. `my-awesome-software`
* `Select github_repository_url:` - Default will be e.g. `https://github.com/adamltyson/my-awesome-software`, but you 
can also provide this later.
* `module_name [my_awesome_software]:` - The default will be the same as `package_name` but with hyphens 
converted to underscores.
* `short_description [A simple Python package]` - Enter a simple, one-line description of your Python package. 
* `Select license:` - choose from:
  - `1 - BSD-3`
  - `2 - MIT`
  - `3 - Mozilla Public License 2.0`
  - `4 - Apache Software License 2.0`
  - `5 - GNU LGPL v3.0`
  - `6 - GNU GPL v3.0`

### To use:

**Installation**
For a local, editable install, in the project directory, run:
```
pip install -e .
```

For a local, editable install with all the development tools (e.g. testing, formatting etc.) run:
```
pip install -e '.[dev]'
```
**Pre-commit hooks**
Running `pre-commit install` will run set up [pre-commit hooks](https://pre-commit.com/) to ensure the code is 
formatted correctly. Currently these are:

* [black](https://black.readthedocs.io/en/stable/) for code structure formatting (maximum line length set to 79)
* [flake8](https://flake8.pycqa.org/en/latest/) to enforce [PEP8](https://www.python.org/dev/peps/pep-0008/)

These will prevent code being committed if any of these hooks fail. To run them individually:
```
black ./
flake8
```

**Automated versioning**

[bump2version](https://github.com/c4urself/bump2version) is used to enforce a consistent style for version numbers,
and create git tags as appropriate.

`.bumpversion.cfg` defines in which files the version will be updated (`setup.cfg`, `<MODULE_NAME>/__init__.py`) and how.

Running `bump2version` will update version numbers throughout the code and, commit the changes to git and tag the commit. The current version is `0.0.1` and there are five version types set up:

* `bump2version patch`, e.g. bump from `0.0.1` to a release candidate `0.0.2rc0`
* `bump2version minor`, e.g. bump from `0.0.1` to a release candidate `0.1.0rc0`
 * `bump2version major`, e.g. bump from `0.0.1` to a release candidate `1.0.0rc0`
* `bump2version rc`, e.g. bump from `0.1.0rc0` to create a new release candidate `0.1.0rc1`
* `bump2version release`, e.g. bump from `0.1.0rc0` to create a new release `0.1.0`

To ensure the tags are pushed to GitHub:

```bash
git push --follow-tags
```

**Test structure**

A [pytest](https://docs.pytest.org/en/7.0.x/) test suite can be run with `pytest`. 
A template structure for this is in `tests`.

**GitHub actions workflow**
A GitHub actions workflow (`.github/workflows/test_and_deploy.yml`) has been set up to run (on each commit/PR):
* Linting checks (black, flake8, mypy).
* Pytest (only if linting checks pass)
* Release to PyPI (only if tests pass). Requires `TWINE_API_KEY` from PyPI to be set in repository secrets.
