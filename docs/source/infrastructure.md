# Infrastructure

## Tests

Write your test methods and classes in the `test` folder. We are using [pytest](https://docs.pytest.org/en/7.2.x/getting-started.html).
In your test module you can call your methods in a simple way:

```python
# filename: test_math.py
from my_awesome_software import math

# here your test function
```

If you're testing a small piece of code, make it a unit test. If you want to test whether two or more software units work well together, create an integration test.

:::{important}
Before committing your changes
:::

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

# Pre-commit hooks

Running `pre-commit install` will set up [pre-commit hooks](https://pre-commit.com/) to ensure the code is
formatted correctly. Currently, these are:
* [ruff](https://github.com/charliermarsh/ruff) does a number of jobs, including linting, auto-formatting code (with `ruff-format`), and sorting import statements.
* [mypy](https://mypy.readthedocs.io/en/stable/index.html) a static type checker
* [check-manifest](https://github.com/mgedmin/check-manifest) to ensure that the right files are included in the pip package.
* [codespell](https://github.com/codespell-project/codespell) to check for common misspellings.


These will prevent code from being committed if any of these hooks fail. To run them individually:
```sh
ruff check --fix   # Lint all files in the current directory, and fix any fixable errors.
ruff format		   # Format all files in the current directory.
mypy -p my_awesome_software
check-manifest
codespell
```

You can also execute all the hooks using
```sh
pre-commit run
```
or
```sh
pre-commit run --all-files
```

 The best time to run this is after you have staged your changes, but before you commit them.

In the case you see `mypy` failing with an error like `Library stubs not installed for this-package`, you do have to edit the `.pre-commit-config.yaml` file by adding the additional dependency to `mypy`:
``` sh
- id: mypy
	additional_dependencies:
		- types-setuptools
		- types-this-package
```

# Versioning

We recommend the use of [semantic versioning](https://semver.org/), which uses a `MAJOR`.`MINOR`.`PATCH` versiong number where these mean:

* PATCH = small bugfix
* MINOR = new feature
* MAJOR = breaking change

## Automated versioning
[`setuptools_scm`](https://github.com/pypa/setuptools_scm) can be used to automatically version your package. It has been pre-configured in the `pyproject.toml` file. [`setuptools_scm` will automatically infer the version using git](https://github.com/pypa/setuptools_scm#default-versioning-scheme). To manually set a new semantic version, create a tag and make sure the tag is pushed to GitHub. Make sure you commit any changes you wish to be included in this version. E.g. to bump the version to `1.0.0`:

```sh
git add .
git commit -m "Add new changes"
git tag -a v1.0.0 -m "Bump to version 1.0.0"
git push --follow-tags
```
:::{tip}
It is also possible to perform this step by using the [GitHub web interface or CLI](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
:::

# GitHub actions workflow

A GitHub actions workflow (`.github/workflows/test_and_deploy.yml`) has been set up to run (on each commit/PR):
* Linting checks (pre-commit).
* Testing (only if linting checks pass)
* Release to PyPI (only if a git tag is present and if tests pass). Requires `TWINE_API_KEY` from PyPI to be set in repository secrets.

This automation ensures that each commit or pull request is validated and that releases are published only when all checks pass.

# Documentation

Software documentation is important for effectively communicating how to use the software to others as well as to your future self.

If you want to include documentation in your package, make sure to respond with `1 - Yes` when prompted during the `cookiecutter` setup. This will instantiate a `docs` folder with a skeleton documentation system, that you can build upon.

The documentation source files are located in the `docs/source` folder and should be written in either [reStructuredText](https://docutils.sourceforge.io/rst.html) or [markdown](https://myst-parser.readthedocs.io/en/stable/syntax/typography.html). The `index.rst` file corresponds to the main page of the documentation website. Other `.rst`  or `.md` files can be included in the main page via the `toctree` directive.

The documentation is built using [Sphinx](https://www.sphinx-doc.org/en/master/) and the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/). The `docs/source/conf.py` file contains the `Sphinx` configuration.

## Building the documentation locally
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

## Publishing the documentation
We have included an extra GitHub actions workflow in `.github/workflows/docs_build_and_deploy.yml` that will build the documentation and deploy it to [GitHub pages](https://pages.github.com/).
* The build step is triggered every time a pull request is opened or a push is made to the `main` branch. This way you can make sure that the documentation does not break before merging your changes.
* The deployment is triggered only when a tag is present (see [Automated versioning](#automated-versioning)). This ensures that new documentation versions are published in tandem with the release of a new package version on PyPI (see [GitHub actions workflow](#github-actions-workflow)).
* The published docs are by default hosted at `https://<github_username_or_organization>.github.io/<package_name>/`. To enable hosting, you will need to go to the settings of your repository, and under the "Pages" section, select the `gh-pages` branch as the source for your GitHub pages site.
* A popular alternative to GitHub pages for hosting the documentation is [Read the Docs](https://readthedocs.org/). To enable hosting on Read the Docs, you will need to create an account on the website and follow the instructions to link your GitHub repository to your Read the Docs account.

## Docstrings and API documentation
The journey towards good documentation starts with writing docstrings for all functions in your module code. In the example `math.py` and `greetings.py` modules you will find some docstrings that you can use as a template. We have written the example docstrings following the [numpy style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html) but you may also choose another widely used style, such as the [Google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

Once you have written docstrings for all your functions, API documentation can be automatically generated via the [Sphinx autodoc extension](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html). We have given examples of how to do this in the `docs/source/api_index.rst` file.
