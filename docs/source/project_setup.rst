Setup
=====

This section describes how to set up your project using cookiecutter.

Installing Cookiecutter
-----------------------

Install Cookiecutter using pip or conda:

.. code-block:: bash

   pip install cookiecutter
   # or with conda:
   conda install -c conda-forge cookiecutter

Creating a Cookiecutter Project
-------------------------------

Run the following command in your target folder:

.. code-block:: bash

   cookiecutter https://github.com/neuroinformatics-unit/python-cookiecutter

You'll be prompted for several configuration options, such as:

- **full_name**: e.g. ``Adam Tyson``
- **email**: e.g. ``cookiecutter@adamltyson.com``
- **github_username_or_organization**: e.g. ``adamltyson``
- **package_name**: e.g. ``my-awesome-software``
- **module_name**: (auto-generated from package_name)
- **short_description**: A brief description of your package
- **license**: Choose from BSD-3, MIT, MPL 2.0, Apache 2.0, GNU LGPL, or GNU GPL
- **create_docs**: Choose whether to generate Sphinx documentation (``1 - Yes``)

Project Structure
-----------------

After running cookiecutter, your project will have a structure similar to:

.. code-block:: text

   my-awesome-software/
   ├── LICENSE
   ├── MANIFEST.in
   ├── README.md
   ├── pyproject.toml
   ├── tox.ini
   ├── my_awesome_software/
   │   └── __init__.py
   └── tests/
       ├── __init__.py
       ├── test_integration/
       │   └── __init__.py
       └── test_unit/
           ├── __init__.py
           └── test_placeholder.py

Initializing a Git Repository
-----------------------------

Navigate to your project folder and initialize git:

.. code-block:: bash

   cd my-awesome-software
   git init -b main

If you’re using an older Git version (<2.28), use:

.. code-block:: bash

   git init
   git checkout -b main

Then, add and commit your changes:

.. code-block:: bash

   git add .
   git commit -m "Initial commit"

Finally, add the remote origin and push to GitHub:

.. code-block:: bash

   git remote add origin git@github.com:adamltyson/my-awesome-software.git
   git push
