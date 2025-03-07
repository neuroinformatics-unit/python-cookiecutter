# modules and tests

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

### Write tests

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
