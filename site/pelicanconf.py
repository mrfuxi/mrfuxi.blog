# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Karol Dulęba'
SITENAME = 'Coding After Hours'
SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

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
    ('Twitter', 'twitter', 'https://twitter.com/MrFuxi'),
    ('GitHub', 'github', 'https://github.com/mrfuxi'),
    ('Google Plus', 'google-plus', 'https://plus.google.com/+KarolDulęba'),
    ('LinkedIn', 'linkedin', 'http://www.linkedin.com/in/dulebakarol'),
    # ('RSS Feed', 'rss', ''),
)

# ToDo: Pagination
DEFAULT_PAGINATION = 100

base_dir = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(base_dir, "theme", "anew")

PLUGINS = ["my_plugins.post_type", ]
PAGE_COLUMNS_LAYOUT = 1

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
