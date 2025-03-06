# conf.py
# Configuration file for the Sphinx documentation builder.
project = 'python cookiecutter'
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
html_logo = "_static/dark-logo-niu.png"
html_static_path = ["_static"]
html_title = "Python Cookiecutter"
html_favicon = "_static/favicon.ico"


html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar.html"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/neuroinformatics-unit/python-cookiecutter",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        {
            "name": "Zulip (chat)",
            "url": "https://neuroinformatics.zulipchat.com/#narrow/channel/406003-Python-cookiecutter",
            "icon": "fa-solid fa-comments",
            "type": "fontawesome",
        },
    ],
    "logo": {
        "text": f"{project}",
    },
    "footer_start": ["footer_start"],
    "footer_end": ["footer_end"],
    "external_links": [],
}

# Sitemap configuration
github_user = "neuroinformatics-unit"
html_baseurl = "https://neuroinformatics-unit.github.io/python-cookiecutter/"
sitemap_url_scheme = "{link}"

  
# -- HTML sidebar configuration ---------------------------------------------
html_sidebars = {
    # Apply sidebar to ALL pages except index
    "**": ["sidebar-nav.html"],  
    "index": []  
}
html_show_sourcelink = False


def setup(app):
    app.add_css_file("css/custom.css")


# What to show on the 404 page
notfound_context = {
    "title": "Page Not Found",
    "body": """
    <h1>Page Not Found</h1>

    <p>Sorry, we couldn't find that page.</p>

    <p>We occasionally restructure the cookiercutter website, and some links may have broken.</p> 

    <p>Try using the search box or go to the homepage.</p>
""",
}

# needed for GH pages (vs readthedocs),
# because we have no '/<language>/<version>/' in the URL
notfound_urls_prefix = None
