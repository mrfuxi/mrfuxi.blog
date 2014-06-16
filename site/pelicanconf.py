# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = "Karol Dulęba"
SITENAME = "Coding After Hours"
SITEURL = ""
SITE_KEYWORDS = """
    Python, Solr, C++, Linux, Docker, Lucene, Django, blog, software development
"""
SITE_DESCRIPTION = """
    Blog about writing software with Python, Solr and the processes around
"""

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

TRANSLATION_FEED_ATOM = None
USE_FOLDER_AS_CATEGORY = False
SUMMARY_MAX_LENGTH = 50
SEARCH = False

MENUITEMS = (
    ("Home", "/"),
)
CATEGORY_URL = "{slug}/"
CATEGORY_SAVE_AS = "{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

ARTICLE_SAVE_AS = "{category}/{slug}/index.html"
ARTICLE_URL = "{category}/{slug}/"
ARTICLE_DIR = os.path.abspath("content")

# Social widget
SOCIAL = (
    ("Twitter", "twitter", "https://twitter.com/MrFuxi"),
    ("GitHub", "github", "https://github.com/mrfuxi"),
    ("Google Plus", "google-plus", "https://plus.google.com/+KarolDulęba"),
    ("LinkedIn", "linkedin", "http://www.linkedin.com/in/dulebakarol"),
    # ("RSS Feed", "rss", ""),
)

# ToDo: Pagination
DEFAULT_PAGINATION = 100

base_dir = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(base_dir, "theme", "anew")


PLUGIN_PATH = 'plugins'
PLUGINS = [
    "my_plugins.post_type",
    "sitemap",
    "liquid_tags.youtube",
    "liquid_tags.vimeo",
]
PAGE_COLUMNS_LAYOUT = 1

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily',
    },
}

MD_EXTENSIONS = ['extra']
HIGHLIGHT_STYLE = 'default'
