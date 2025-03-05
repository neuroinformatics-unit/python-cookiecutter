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
