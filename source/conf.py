#!/usr/bin/env python3
import datetime
import sphinx_rtd_theme

# The 3Di release name that's shown at the top of the sidebar.
# Note: non-production documentation builds are marked as such, you don't need
# to change the release name for that.
# Removed version to prevent release from being outdated.
# Last THREEDI_RELEASE value was 2022-02 Klondike Release.
THREEDI_RELEASE = ""


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
#needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.todo"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "3Di"
current_year = datetime.date.today().year
copyright = str(current_year) + ", Nelen & Schuurmans"
author = "Nelen & Schuurmans"

documentation_version = open("../version.txt").readlines()[0].strip()
is_development_build = "dev" in documentation_version
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = THREEDI_RELEASE
if is_development_build:
    version += " (dev doc %s)" % datetime.date.today()
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']
html_css_files = ['stylesheet.css',]
html_js_files = [
    'matomo.js',
]
html_css_files = [
    'css/custom.css',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = is_development_build


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
numfig = True
if not is_development_build:
    # Only use google analytics on the production doc site.
    html_theme_options = {"analytics_id": "UA-111119907-2"}


# Latex output settings, mostly to get unicode characters in math working.
latex_engine = "xelatex"
latex_elements = {
    "papersize": "a4paper",
    "extrapackages": r"\usepackage{unicode-math}",
    # The next two are to prevent the html "align" from wreaking pdf output.
    # See https://github.com/sphinx-doc/sphinx/issues/3289#issuecomment-298942353
    "figure_align": "H",
    'preamble': r'\renewenvironment{wrapfigure}[2]{\begin{figure}[H]}{\end{figure}}',
}
