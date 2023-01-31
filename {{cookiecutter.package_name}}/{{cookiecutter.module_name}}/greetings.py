# Define an example class to demonstrate
# Sphinx's autodoc and autosummary features:
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
# https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html

# Docstrings are written in NumPy format:
# https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html


class Greetings:
    """
    A simple example class

    Attributes
    ----------
    name : str
        The name of the person to greet

    Methods
    -------
    say_hello
        Say hello to the person
    say_goodbye
        Say goodbye to the person
    """

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        """
        Say hello to the person
        """
        print(f"Hello {self.name}!")

    def say_goodbye(self):
        """
        Say goodbye to the person
        """
        print(f"Goodbye {self.name}!")
