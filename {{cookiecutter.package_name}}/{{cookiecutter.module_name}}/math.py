# Define some example functions to demonstrate
# Sphinx's autodoc and autosummary features:
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
# https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html

# Docstrings are written in NumPy format:
# https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html


def add_two_integers(a: int, b: int) -> int:
    """Add two integer numbers.

    Parameters
    ----------
    a : int
        The first number.
    b : int
        The second number.

    Returns
    -------
    int
        The sum of the two numbers.
    """
    return a + b


def subtract_two_integers(a: int, b: int) -> int:
    """Subtract two integer numbers.

    Parameters
    ----------
    a : int
        The first number.
    b : int
        The second number.

    Returns
    -------
    int
        The difference of the two numbers.
    """
    return a - b
