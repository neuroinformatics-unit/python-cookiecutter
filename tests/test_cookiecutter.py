import copy
import os
import platform
import subprocess
from pathlib import Path

import pytest
import ruamel.yaml
import toml
import yaml

# dependencies
# pyyaml
# cookiecutter
# pytest
# toml

COOKIECUTTER_DIR = Path(__file__).parent.parent
CONFIG_FILENAME = COOKIECUTTER_DIR / "tests" / "cookiecutter_test_configs.yaml"

def create_test_configs(create_docs=False):
    test_dict = {
        "default_context": {
            "full_name": "Test Cookiecutter",
            "email": "testing@cookiecutter.com",
            "github_username_or_organization": "test_cookiecutter_username",
            "package_name": "test-cookiecutter",
            "github_repository_url": "https://github.com/test_cookiecutter_username/test-cookiecutter",
            "module_name": "test_cookiecutter_module",
            "short_description": "Lets Test CookierCutter",
            "license": "BSD-3",
            "create_docs": create_docs,
        },
    }

    with open(CONFIG_FILENAME, "w") as config_file:
        yaml.dump(test_dict, config_file, sort_keys=False)

    return test_dict["default_context"]


@pytest.fixture(scope="function") 
def package_path_config_dict(tmp_path):

    config_dict = create_test_configs(create_docs=False)

    os.chdir(tmp_path)
    
    subprocess.run(f"cookiecutter {COOKIECUTTER_DIR} --config-file {CONFIG_FILENAME} --no-input", shell=True)

    package_path = tmp_path / config_dict["package_name"]

    return package_path, config_dict
        

@pytest.fixture(scope="function")
def pip_install(package_path_config_dict):

    package_path, config_dict = package_path_config_dict

    uninstall_cmd = f"pip uninstall -y {config_dict['package_name']}"
    dev_formatting = ".[dev]" if platform.system() == "Windows" else "'.[dev]'"
    install_cmd = f"pip install -e {dev_formatting}"

    # Installs the package using pip
    os.chdir(package_path)

    # Uninstall and check package not installed
    subprocess.run("git init", shell=True)

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
    subprocess.run(install_cmd, shell=True)
    yield config_dict
    # Uninstall package
    subprocess.run(uninstall_cmd, shell=True)


def test_directory_names(package_path_config_dict):

    package_path = package_path_config_dict[0]

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

def test_docs():
    """
    First take the
    """
    ## do some tests
   # b#
    #create_test_configs(create_docs=True)

    # do some other tests


def test_pyproject_toml(package_path_config_dict):
    """
    """
    package_path, config_dict = package_path_config_dict

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

    if config_dict["create_docs"]:
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
        "isort",
        "mypy",
        "pre-commit",
        "flake8",
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

    assert (
        project_toml["tool"]["pytest"]["ini_options"]["addopts"]
        == "--cov=test_cookiecutter"
    )
    assert project_toml["tool"]["black"]


def test_pip_install(pip_install):

    config_dict = pip_install  

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