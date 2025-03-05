# conf.py
# Configuration file for the Sphinx documentation builder.
project = 'cookiecutter-python'
copyright = "2025, Neuroinformatics Unit"
author = 'NIU'
release = "1.0.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    "nbsphinx",
]

# Configure MyST Parser
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
    "attrs_inline"
]

myst_heading_anchors = 4

source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext'
}

templates_path = ['_templates']
exclude_patterns = [
    "**.ipynb_checkpoints",
    "**/includes/**",
]

# -- HTML output options -----------------------------------------------------
html_theme = 'pydata_sphinx_theme'
html_logo = "_static/logo.png"
html_static_path = ["_static"]
html_title = "Python Cookiecutter"
html_favicon = "_static/favicon.ico"
html_show_sourcelink = False

html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar.html"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/neuroinformatics-unit/python-cookiecutter",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        }
    ],
    "logo": {
        "text": "Python Cookiecutter",
        "image_light": "logo.png",
        "image_dark": "logo.png",
    },
    "show_nav_level": 2,
    "navigation_depth": 3,
    "collapse_navigation": True,
}

# Sitemap configuration
html_baseurl = "https://neuroinformatics-unit.github.io/python-cookiecutter/"
sitemap_url_scheme = "{link}"

  
html_sidebars = {
    "**": ["sidebar-nav.html"]
}

def setup(app):
    app.add_css_file("css/custom.css")
