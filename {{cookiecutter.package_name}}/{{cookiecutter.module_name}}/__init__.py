from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{cookiecutter.package_name}}")
except PackageNotFoundError:
    # package is not installed
    pass
