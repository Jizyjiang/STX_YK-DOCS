# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '音控室 说明手册'
copyright = '2022 IN1.TECH'
author = '蒋易银'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.video',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
import sphinx_theme
html_theme = 'stanford_theme'
html_theme_path = [sphinx_theme.get_html_theme_path('stanford-theme')]

# -- Options for EPUB output
epub_show_urls = 'footnote'
