# Project Setup

This section describes how to set up your project using cookiecutter.

## Installation & Setup

First, install cookiecutter in your desired environment. Running in the terminal in your environment:

:::{note}
You must have Python installed to use Cookiecutter
:::

using pip or conda:

::::{tab-set}
:::{tab-item} pip
Install using pip
```sh
pip install cookiecutter
```
:::
:::{tab-item} conda
Install using conda
```sh
conda install -c conda-forge cookiecutter
```
:::
::::


## Creating a Cookiecutter Project

In the folder or directory, you want to create the project:


Then Run the following command:

```sh
cookiecutter https://github.com/neuroinformatics-unit/python-cookiecutter
```

You will be then asked a series of questions about how you want to set up your project.

For each one, type your answer, enter a single number (or just hit return) to choose from a default option.

such as:


* `full_name [Python developer]:` - e.g. `Adam Tyson`
* `email [yourname@example.com]:` - e.g. `cookiecutter@adamltyson.com`
* `github_username_or_organization [githubuser]:` - e.g. `adamltyson`
* `package_name [python-package]:` - e.g. `my-awesome-software`
* `Select github_repository_url:` - Default will be e.g. `https://github.com/<your-username>/my-awesome-software`, but you can also provide this later.
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

:::{important}
If you respond positively to `Select create_docs:`, an additional `docs` folder will be created and two example Python modules (`math.py` and `greetings.py`) will be added to the above structure.
:::

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

## Creating a GitHub Repository

1. **Sign In to GitHub:** Visit [GitHub](https://github.com) and sign in with your account.


2. **Create a New Repository:**

    - Click on the **+** icon in the upper-right corner of the page and select **New repository**.
    - Alternatively, you can navigate directly to: [New Repository](https://github.com/new)

3. **Fill in Repository Details:**

    - **Repository Name:** Enter a name for your project (e.g: ``my-awesome-software``).
    - **Description:** Optionally, provide a short description of your project.
    - **Repository Visibility:** Choose between **Public** or **Private**.

    - **Initialize Repository:** You may leave the repository empty (without a README, .gitignore, or license) if you plan to push your existing local project. If you prefer, you can initialize it with a README file.

:::{warning}
If you initialize with a README, you will need to pull those changes before pushing your local repository.
:::

4. **Create the Repository:** Click the **Create repository** button. GitHub will then create your new repository and provide you
    with the repository URL (e.g.``https://github.com/your-username/my-awesome-software.git``).

## Initializing a Git Repository

:::{note}
When creating a cookiecutter project, it asks for a GitHub username or organization and package name. However this does not initialize a git repository.
:::

Navigate to your project folder and initialize git:

```sh
cd my-awesome-software
```
```sh
git init -b main
```

If you're using an older Git version (``<2.28``), use:

```sh
git init
```
```sh
git checkout -b main
```

Then, add and commit your changes:

```sh
git add .
```
```sh
git commit -m "Initial commit"
```

Finally, add the remote origin and push to GitHub:

```sh
git remote add origin https://github.com/<your-username>/my-awesome-software.git
```
```sh
git push --set-upstream origin main
```
That\'s it! Your project is now set up and ready to go. 🚀

# Modules and Tests

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

## Add dependencies
To ensure any dependencies are installed at the same time as installing
your package, add them to your `pyproject.toml` file. E.g. to add `numpy`
and `pandas` as dependencies, add them to the `dependencies = []` list under
the `[project]` heading:

```toml
dependencies = ["numpy", "pandas"]
```

## Write tests

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
