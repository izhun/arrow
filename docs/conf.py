# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "arrow"
copyright = "2019, Chris Smith"
author = "Chris Smith"

release = "0.14.0"

# -- General configuration ---------------------------------------------------

extensions = ["sphinx.ext.autodoc"]

templates_path = []

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

master_doc = "index"
source_suffix = ".rst"
pygments_style = "sphinx"

language = None

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"
html_theme_path = []
html_static_path = []

html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True

html_theme_options = {
    "description": "Arrow is a sensible and human-friendly approach to dates, times, and timestamps.",
    "github_user": "crsmithdev",
    "github_repo": "arrow",
    "github_banner": True,
    "show_related": False,
    "show_powered_by": False,
}

html_sidebars = {
    "**": ["about.html", "localtoc.html", "relations.html", "searchbox.html"]
}
