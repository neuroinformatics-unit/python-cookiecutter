from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("python-packaging-at")
except PackageNotFoundError:
    # package is not installed
    pass
