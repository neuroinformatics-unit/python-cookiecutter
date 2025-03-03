Contributing to cookiecutter-python
=====================================

Thank you for considering contributing to cookiecutter-python!
We welcome contributions that improve the project, whether it’s code, documentation, or enhancements.
Please follow the guidelines below to ensure a smooth process.

Workflow
--------

1. **Fork and Clone the Repository**
   Fork the main repository on GitHub, then clone your fork locally:

   .. code-block:: bash

      git clone https://github.com/<your-username>/python-cookiecutter.git
      cd python-cookiecutter

2. **Create a New Branch**
   Create and switch to a new branch for your changes:

   .. code-block:: bash

      git checkout -b my_new_feature

3. **Make Your Changes**
   Edit the website content, code, or documentation as needed.
   When you’re ready, add and commit your changes with a descriptive message:

   .. code-block:: bash

      git add .
      git commit -m "Describe your changes here"

4. **Push Your Branch and Create a Pull Request**
   Push the new branch to GitHub:

   .. code-block:: bash

      git push origin --set-upstream origin my_new_feature

   Then, open a pull request against the `main` branch of the main repository.
   This will automatically trigger a GitHub Action to verify that the website builds correctly.

5. **Review and Merge**
   If the build checks pass, assign someone to review your pull request.
   Once approved and merged into the `main` branch, another GitHub Action will build the website and publish it to the `gh-pages` branch.

6. **Deployment**
   After merging, the updated website will be available at:
   `python-cookiecutter.github.io`

Local Testing
-------------

Before pushing your changes, you can test the website locally:

- **First-Time Setup:**
  Install the required dependencies and build the site:

  .. code-block:: bash

      pip install -r docs/requirements.txt
      sphinx-build docs/source docs/build

Alternatively, you can use the following commands to install the dependencies and build the site:

  .. code-block:: bash

      pip install -r docs/requirements.txt
      cd docs
      make html

- **Rebuilding the Site:**
  Each time you update the documentation, rebuild the site by running:

  .. code-block:: bash

      rm -rf docs/build && sphinx-build docs/source docs/build

  Then, open ``docs/build/index.html`` in your browser to preview the changes.

Additional Guidelines
---------------------

- **Coding Standards:** Ensure that your contributions follow the project's coding and documentation guidelines.
- **Commit Messages:** Write clear and concise commit messages.
- **Documentation:** If your changes affect the website or project behavior, please update the documentation accordingly.

Thank you for your contributions!
