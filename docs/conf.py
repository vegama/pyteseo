# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from pyteseo.__init__ import __version__

project = "pyTESEO"
copyright = "2022, Germán Aragón Caminero"
author = "Germán Aragón Caminero"
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "autoapi.extension",
    "sphinx_rtd_theme",
    "myst_nb",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
# html_theme = 'furo'
# html_theme = 'sphinx_book_theme'

html_static_path = ["_static"]
html_logo = "_static/pyTESEO_logo.png"
html_title = project + " v" + release

# -- Options for autoapi ext -------------------------------------------------

autoapi_modules = {"pyteseo": None}
autoapi_dirs = ["../pyteseo"]
autoapi_ignore = ["*/test_*.py"]
# autoapi_add_toctree_entry = False
