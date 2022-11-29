from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("test-cookiecutter")
except PackageNotFoundError:
    # package is not installed
    pass
