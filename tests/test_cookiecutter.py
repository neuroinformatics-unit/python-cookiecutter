import os
import platform
import subprocess
from pathlib import Path

import pytest
import toml
import yaml

# dependencies
# pyyaml
# cookiecutter
# pytest
# toml

COOKIECUTTER_DIR = Path(__file__).parent.parent
CONFIG_FILENAME = COOKIECUTTER_DIR / "tests" / "cookiecutter_test_configs.yaml"


with open(f"{CONFIG_FILENAME}", "r") as config_file:
    config_dict = yaml.full_load(config_file)

config_dict = config_dict["default_context"]


@pytest.fixture(autouse=True, scope="session")
def package_path(tmp_path_factory):
    # Runs cookiecutter in a temporary directory, and returns
    # that directory.
    tmp_path = tmp_path_factory.mktemp("package")
    os.chdir(tmp_path)
    subprocess.run(
        f"cookiecutter {COOKIECUTTER_DIR} --config-file "
        f"{CONFIG_FILENAME} --no-input",
        shell=True,
    )

    return tmp_path / config_dict["package_name"]


@pytest.fixture(autouse=True, scope="session")
def pip_install(package_path):
    # Installs the package using pip
    os.chdir(package_path)

    # Uninstall and check package not installed
    subprocess.run("git init", shell=True)
    uninstall_cmd = f"pip uninstall -y {config_dict['package_name']}"
    subprocess.run(uninstall_cmd, shell=True)
    result = subprocess.Popen(
        f"pip show {config_dict['package_name']}",
        shell=True,
        stderr=subprocess.PIPE,
    )
    __, stderr = result.communicate()
    assert (
        f"WARNING: Package(s) not found: "
        f"{config_dict['package_name']}" in stderr.decode("utf8")
    )

    # Install package
    dev_formatting = ".[dev]" if platform.system() == "Windows" else "'.[dev]'"
    cmd = f"pip install -e {dev_formatting}"
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    stdout, __ = result.communicate()
    yield

    # Uninstall package
    subprocess.run(uninstall_cmd, shell=True)


def test_directory_names(package_path):
    assert package_path.exists()
    expected = [
        # Files
        ".github",
        ".gitignore",
        ".pre-commit-config.yaml",
        "LICENSE",
        "MANIFEST.in",
        "pyproject.toml",
        "README.md",
        "tox.ini",
        Path("test_cookiecutter") / "__init__.py",
        # Directories
        "test_cookiecutter",
        "tests",
    ]

    for f in expected:
        assert (package_path / f).exists()


def test_pyproject_toml(package_path):
    pyproject_path = package_path / "pyproject.toml"
    project_toml = toml.load(pyproject_path.as_posix())

    assert project_toml["project"]["name"] == config_dict["package_name"]

    # some of these are hard coded from the cookiecutter
    # pyproject.toml has not asked user for
    assert (
        project_toml["project"]["authors"][0]["name"]
        == config_dict["full_name"]
    )
    assert (
        project_toml["project"]["authors"][0]["email"] == config_dict["email"]
    )
    assert project_toml["project"]["description"] == "A simple Python package"

    assert project_toml["project"]["readme"] == "README.md"
    assert project_toml["project"]["requires-python"] == ">=3.8.0"
    assert (
        project_toml["project"]["license"]["text"] == "BSD-3-Clause"
    )  # parameterize this? test if url not given?

    assert project_toml["project"]["classifiers"] == [
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ]

    assert (
        project_toml["project"]["urls"]["homepage"]
        == config_dict["github_repository_url"]
    )
    assert (
        project_toml["project"]["urls"]["bug_tracker"]
        == config_dict["github_repository_url"] + "/issues"
    )
    assert (
        project_toml["project"]["urls"]["documentation"]
        == config_dict["github_repository_url"]
    )
    assert (
        project_toml["project"]["urls"]["source_code"]
        == config_dict["github_repository_url"]
    )
    assert (
        project_toml["project"]["urls"]["user_support"]
        == config_dict["github_repository_url"] + "/issues"
    )

    assert len(project_toml["project"]["optional-dependencies"].keys()) == 1
    assert project_toml["project"]["optional-dependencies"]["dev"] == [
        "pytest",
        "pytest-cov",
        "coverage",
        "tox",
        "black",
        "mypy",
        "pre-commit",
        "ruff",
        "setuptools_scm",
    ]

    assert project_toml["build-system"]["requires"] == [
        "setuptools>=45",
        "wheel",
        "setuptools_scm[toml]>=6.2",
    ]

    assert (
        project_toml["build-system"]["build-backend"]
        == "setuptools.build_meta"
    )

    assert project_toml["tool"]["setuptools"]["packages"]["find"][
        "include"
    ] == ["test_cookiecutter*"]
    assert project_toml["tool"]["setuptools"]["packages"]["find"][
        "exclude"
    ] == ["tests*"]

    assert (
        project_toml["tool"]["pytest"]["ini_options"]["addopts"]
        == "--cov=test_cookiecutter"
    )
    assert project_toml["tool"]["black"]


def test_pip_install(pip_install):
    result = subprocess.Popen(
        f"pip show {config_dict['package_name']}",
        shell=True,
        stdout=subprocess.PIPE,
    )
    stdout, __ = result.communicate()

    # Home-page is not in pip show output...
    show_details = stdout.decode("utf8")
    assert "Name: test-cookiecutter" in show_details
    assert "Version: 0.1.dev0" in show_details
    assert "Summary: A simple Python package" in show_details
    assert (
        "Author-email: Test Cookiecutter <testing@cookiecutter.com>"
        in show_details
    )
    assert "License: BSD-3-Clause" in show_details
