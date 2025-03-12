# Contributing

Thank you for considering contributing to python-cookiecuttter! We welcome contributions that improve the project, whether it's code,
documentation, or anything else.

:::{note}
To discuss contributing, you can join the [Zulip Channel](https://neuroinformatics.zulipchat.com/#narrow/channel/406003-Python-cookiecutter) here.
:::

Please follow the guidelines below to ensure a smooth process.

1. **Fork and Clone the Repository** Fork the main repository on
    GitHub, then clone your fork locally:

    ``` sh
    git clone https://github.com/<your-username>/python-cookiecutter.git
    cd python-cookiecutter
    ```

2. **Create a New Branch** Create and switch to a new branch for your
    changes:

    ``` sh
    git checkout -b my_new_feature
    ```

3. **Make Your Changes** Edit the content, code, or
    documentation as needed. When you're ready, add and commit your
    changes with a descriptive message:

    ``` sh
    git add .
    git commit -m "Describe your changes in short here"
    ```

4. **Push Your Branch and Create a Pull Request** Push the new branch
    to GitHub:

    ``` sh
    git push origin --set-upstream origin my_new_feature
    ```

    Then, open a pull request against the ``main`` branch of the main repository. This will automatically trigger a GitHub Action to verify that the builds correctly.

5. **Review and Merge** If the build checks pass, assign someone to review your pull request. Once approved and merged into the ``main`` branch, another GitHub Action will build and add your changes to the ``main`` branch.


## Documentation Local Testing

If you are contributing to the Documentation, Before pushing your changes, you can test locally:

-   **First-Time Setup:** Install the required dependencies and build
    the docs:

    ``` sh
    pip install -r docs/requirements.txt
    sphinx-build docs/source docs/build
    ```

Alternatively, you can use the following commands to install the
dependencies and build the docs:

 ``` sh
pip install -r docs/requirements.txt
cd docs
make html
```

- **Rebuilding:** Each time you update the documentation,
    rebuild the docs by running:

    ``` sh
    rm -rf docs/build && sphinx-build docs/source docs/build
    ```
    or

    ```sh
    cd docs
    make clean && make html
    ```

    Then, open `docs/build/index.html` in your browser to preview the changes.
