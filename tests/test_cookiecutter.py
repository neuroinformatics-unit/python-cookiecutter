import os
import subprocess
import tempfile
from pathlib import Path

import toml
import yaml

# dependencies
# pyyaml
# cookiecutter
# pytest
# toml


TEST_DIR = Path(tempfile.mkdtemp())
COOKIECUTTER_DIR = Path.cwd()
CONFIG_FILENAME = COOKIECUTTER_DIR / "tests" / "cookiecutter_test_configs.yaml"


class TestCookieCutter:
    @staticmethod
    def setup_cookiecutter():
        os.chdir(TEST_DIR)
        subprocess.run(
            f"cookiecutter {COOKIECUTTER_DIR} --config-file "
            f"{CONFIG_FILENAME} --no-input",
            shell=True,
        )

    def load_configs(self):
        with open(f"{CONFIG_FILENAME}", "r") as config_file:
            config_dict = yaml.full_load(config_file)
        config_dict = config_dict["default_context"]

        return config_dict

    def test_directory_names(self):
        config_dict, package_path = self.setup_paths()

        assert package_path.exists()
        assert (package_path / ".flake8").exists()
        assert (package_path / ".github").exists()
        assert (package_path / ".gitignore").exists()
        assert (package_path / ".pre-commit-config.yaml").exists()
        assert (package_path / "LICENSE").exists()
        assert (package_path / "MANIFEST.in").exists()
        assert (package_path / "pyproject.toml").exists()
        assert (package_path / "README.md").exists()
        assert (package_path / "tox.ini").exists()

        assert (package_path / "test_cookiecutter").exists()
        assert (package_path / "test_cookiecutter" / "__init__.py").exists()

        assert (package_path / "tests").exists()

    def check_pyproject_toml(self):
        config_dict, package_path = self.setup_paths()

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
            project_toml["project"]["authors"][0]["email"]
            == config_dict["email"]
        )
        assert (
            project_toml["project"]["description"] == "A simple Python package"
        )

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
            == config_dict["ghpages_docs_url"]
        )
        assert (
            project_toml["project"]["urls"]["source_code"]
            == config_dict["github_repository_url"]
        )
        assert (
            project_toml["project"]["urls"]["user_support"]
            == config_dict["github_repository_url"] + "/issues"
        )

        assert (
            len(project_toml["project"]["optional-dependencies"].keys()) == 1
        )
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
        assert project_toml["tool"]["setuptools"]["packages"]["find"][
            "exclude"
        ] == ["tests", "docs*"]

        assert (
            project_toml["tool"]["pytest"]["ini_options"]["addopts"]
            == "--cov=test_cookiecutter"
        )
        assert project_toml["tool"]["black"]

    def test_pip_install(self):
        config_dict, package_path = self.setup_paths()

        os.chdir(package_path)
        subprocess.run("git init", shell=True)
        subprocess.run(
            f"pip uninstall -y {config_dict['package_name']}", shell=True
        )
        result = subprocess.Popen(
            f"pip show {config_dict['package_name']}",
            shell=True,
            stderr=subprocess.PIPE,
        )

        # check package definitely not already installed
        __, stderr = result.communicate()
        assert (
            f"WARNING: Package(s) not found: "
            f"{config_dict['package_name']}" in stderr.decode("utf8")
        )

        # install package and check correct install
        stdout = self.pip_install()

        # if using zsh
        if "no matches found" in stdout.decode("utf8"):
            self.pip_install(zsh=True)

        # install package and check correct install
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

    def setup_paths(self):
        config_dict = self.load_configs()
        package_path = TEST_DIR / config_dict["package_name"]
        return config_dict, package_path

    @staticmethod
    def pip_install(zsh=False):
        if zsh:
            cmd = "pip install -e '.[dev]'"
        else:
            cmd = "pip install -e .[dev]"
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        stdout, __ = result.communicate()
        return stdout


tester = TestCookieCutter()
tester.setup_cookiecutter()
tester.test_directory_names()
tester.check_pyproject_toml()
tester.test_pip_install()
