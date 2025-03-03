# conf.py

# -- Project information -----------------------------------------------------
project = 'cookiecutter-python'
author = 'Name'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon"
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "linkify",
    "substitution",
    "tasklist",
]

source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext'
}

templates_path = ['_templates']

# -- HTML output options -----------------------------------------------------
html_theme = 'pydata_sphinx_theme'
html_logo = "_static/logo.png"
html_static_path = ["_static"]

html_theme_options = {
    # Disable right sidebar TOC
    "show_toc_level": 0,
    
    # Configure navbar
    "navbar_start": [],
    "navbar_center": ["navbar.html"],
    "navbar_end": [],
    
    # Disable default right sidebar
    "secondary_sidebar_items": [],
    
    # Keep other settings
    "show_nav_level": 2,
    "navigation_depth": 3,
    "collapse_navigation": False,
}

html_sidebars = {
    "**": ["sidebar-nav.html", "search-field.html"]
}

def setup(app):
    app.add_css_file("css/custom.css")