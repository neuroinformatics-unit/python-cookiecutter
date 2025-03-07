# Versioning

We recommend the use of [semantic versioning](https://semver.org/), which uses a `MAJOR`.`MINOR`.`PATCH` versiong number where these mean:

* PATCH = small bugfix
* MINOR = new feature
* MAJOR = breaking change

## Automated versioning
[`setuptools_scm`](https://github.com/pypa/setuptools_scm) can be used to automatically version your package. It has been pre-configured in the `pyproject.toml` file. [`setuptools_scm` will automatically infer the version using git](https://github.com/pypa/setuptools_scm#default-versioning-scheme). To manually set a new semantic version, create a tag and make sure the tag is pushed to GitHub. Make sure you commit any changes you wish to be included in this version. E.g. to bump the version to `1.0.0`:

```sh
git add .
git commit -m "Add new changes"
git tag -a v1.0.0 -m "Bump to version 1.0.0"
git push --follow-tags
```
:::{tip}
It is also possible to perform this step by using the [GitHub web interface or CLI](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
:::
