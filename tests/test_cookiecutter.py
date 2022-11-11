import pathlib
import toml
import pytest
import subprocess
import yaml
import pathlib
import os
import shutil
# dependencies
# pyyaml
# cookiecutter
# pytest


TEST_DIR = pathlib.Path("/Users/joeziminski/data/cookiecutter")  # change now config in tests dir and use pytest tmpdir for tests
CONFIG_FILENAME = "cookiecutter_test_configs.yaml"
COOKIECUTTER_URL = "https://github.com/SainsburyWellcomeCentre/python-cookiecutter.git --checkout porting_to_pyproject.toml"
COOKIECUTTER_CUT_URL = "https://github.com/SainsburyWellcomeCentre/python-cookiecutter.git"

class TestCookieCutter:

    def setup_cookiercutter(self):
        os.chdir(TEST_DIR)
        if os.path.isdir(TEST_DIR / "test-cookiecutter"):  # TODO: config
            shutil.rmtree(TEST_DIR / "test-cookiecutter")

        subprocess.run(f"cookiecutter {COOKIECUTTER_URL} --config-file {TEST_DIR / CONFIG_FILENAME} --no-input", shell=True)

    def load_configs(self):
        """"""
        with open(TEST_DIR / CONFIG_FILENAME, "r") as config_file:
            config_dict = yaml.full_load(config_file)
        config_dict = config_dict["default_context"]

        return config_dict

    def test_directory_names(self):
        """"""
        config_dict = self.load_configs()
        package_path = TEST_DIR / config_dict["package_name"]

        assert os.path.isdir(package_path)
        assert os.path.isfile(package_path / ".bumpversion.cfg")
        assert os.path.isfile(package_path / ".flake8")
        assert os.path.isdir(package_path / ".github")
        assert os.path.isfile(package_path / ".gitignore")
        assert os.path.isfile(package_path / ".pre-commit-config.yaml")
        assert os.path.isfile(package_path / "LICENSE")
        assert os.path.isfile(package_path / "MANIFEST.in")
        assert os.path.isfile(package_path / "pyproject.toml")
        assert os.path.isfile(package_path / "README.md")

        assert os.path.isdir(package_path / "test_cookiecutter")  # TODO: why is this underscore?
        assert os.path.isfile(package_path / "test_cookiecutter" / "__init__.py")

        # assert not os.path.isdir(package_path / "tests") FAILING

    def check_pyproject_toml(self):

        config_dict = self.load_configs()
        package_path = TEST_DIR / config_dict["package_name"]  # TODO: copy from above

        pyproject_path =  package_path / "pyproject.toml"
        project_toml = toml.load(pyproject_path.as_posix())

        assert project_toml["project"]["name"] == config_dict["package_name"]

        # some of these are hard coded from the cookiecutter pyproject.toml as not asked user for
        assert project_toml["project"]["version"] == "0.0.1" # TODO: could not load this in config
        assert project_toml["project"]["authors"][0]["name"] == config_dict["full_name"]
        assert project_toml["project"]["authors"][0]["email"] == config_dict["email"]
        assert project_toml["project"]["description"] == "A simple Python package"

        assert project_toml["project"]["readme"] == "README.md"
        assert project_toml["project"]["requires-python"] == ">=3.8.0"
        assert project_toml["project"]["license"]["text"] == "BSD-3-Clause"  # parameterize this? test if url not given?

        assert project_toml["project"]["classifiers"] == ["Development Status :: 2 - Pre-Alpha",
                                                          "Programming Language :: Python",
                                                          "Programming Language :: Python :: 3",
                                                          "Programming Language :: Python :: 3.7",
                                                          "Programming Language :: Python :: 3.8",
                                                          "Programming Language :: Python :: 3.9",
                                                          "Programming Language :: Python :: 3.10",
                                                          "Operating System :: OS Independent",
                                                          "License :: OSI Approved :: BSD License"]

        assert project_toml["project"]["urls"]["homepage"] == config_dict["github_repository_url"]
        assert project_toml["project"]["urls"]["bug_tracker"] == config_dict["github_repository_url"] + "/issues"
        assert project_toml["project"]["urls"]["documentation"] == config_dict["github_repository_url"]
        assert project_toml["project"]["urls"]["source_code"] == config_dict["github_repository_url"]
        assert project_toml["project"]["urls"]["user_support"] == config_dict["github_repository_url"] + "/issues"

        assert len(project_toml["options"]["extras_require"].keys()) == 1
        assert project_toml["options"]["extras_require"]["dev"] == ["black",
                                                                    "pytest",
                                                                    "pytest-cov",
                                                                    "bump2version",
                                                                    "pre-commit",
                                                                    "flake8",
                                                                    "coverage"]

        assert project_toml["build-system"]["requires"] == ["setuptools>=45",
                                                            "wheel",
                                                            "setuptools_scm[toml]>=6.2"]

        assert project_toml["build-system"]["build-backend"] == "setuptools.build_meta"

        assert project_toml["tool"]["setuptools"]["packages"]["find"]["where"] == ["test_cookiecutter"]
        assert project_toml["tool"]["setuptools"]["packages"]["find"]["exclude"] == ['test-cookiecutter.test*']

        assert project_toml["tool"]["pytest"]["ini_options"]["addopts"] == "--cov=test-cookiecutter"
        assert project_toml["tool"]["black"]

    def test_pip_install(self):

        config_dict = self.load_configs()
        package_path = TEST_DIR / config_dict["package_name"]  # TODO: copy from above

        os.chdir(package_path)
        subprocess.run(f"pip uninstall -y {config_dict['package_name']}", shell=True)
        result = subprocess.Popen(f"pip show {config_dict['package_name']}", shell=True,
                                  stderr=subprocess.PIPE)  # TODO: maybe platform dependent

        # check package definately not already installed
        __, stderr = result.communicate()
        assert f"WARNING: Package(s) not found: {config_dict['package_name']}" in stderr.decode("utf8")

        # install package and check correct install
        result = subprocess.Popen(f"pip install -e '.[dev]'", shell=True,
                                  stdout=subprocess.PIPE)  # TODO: maybe platform dependent
        stdout, __ = result.communicate()
        assert "Successfully installed test-cookiecutter-0.0.1" in stdout.decode("utf8")

        # install package and check correct install
        result = subprocess.Popen(f"pip show {config_dict['package_name']}", shell=True,
                                  stdout=subprocess.PIPE)
        stdout, __ = result.communicate()

        # Home-page is not in pip show output...
        show_details = stdout.decode("utf8")
        assert "Name: test-cookiecutter" in show_details
        assert "Version: 0.0.1" in show_details
        assert "Summary: A simple Python package" in show_details
        assert "\nAuthor: \nAuthor-email: Test Cookiecutter <testing@cookiecutter.com>" in show_details
        assert "License: BSD-3-Clause" in show_details

tester = TestCookieCutter()
tester.setup_cookiercutter()
tester.test_directory_names()
tester.check_pyproject_toml()
tester.test_pip_install()