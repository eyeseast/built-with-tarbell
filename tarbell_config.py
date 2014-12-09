# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""
import datetime
from dateutil.parser import parse as date_parse
from flask import Blueprint

from metalsmyth import Stack
from metalsmyth.plugins.dates import Dates
from metalsmyth.plugins.markup import Markdown

# blueprint
blueprint = Blueprint('bwt', __name__)

# stack setup
stack = Stack('_posts', '_site', 
    Dates('date'), 
    Markdown(output_mode='html5')
)

@blueprint.app_context_processor
def add_stack():
    """
    Add posts to context, sorted by filename.
    For better sorting, use `sort` filter.
    """
    return {'posts': stack.iter()}


@blueprint.app_template_filter('date')
def date_format(s, format=None):
    "Parse and format date string or Excel serial date"

    # handle Excel serial dates
    if isinstance(s, (int, float)):
        tt = xlrd.xldate_as_tuple(s, 0) # 1900-based
        date = datetime.datetime(*tt)

    # handle strings of various kinds
    elif isinstance(s, basestring):
        date = date_parse(s)

    # if it's already a date, just move on
    elif isinstance(s, (datetime.datetime, datetime.date)):
        date = s
    
    # format if we have a format
    if format is not None:
        return date.strftime(format)
    
    return date


# Google spreadsheet key
SPREADSHEET_KEY = "1hmwdXii05aNvPKRIfI2LXQr0HvUphcFz2zJNRoCC2-E"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Spreadsheet cache lifetime in seconds. (Default: 4)
# SPREADSHEET_CACHE_TTL = 4

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# Get context from a local file or URL. This file can be a CSV or Excel
# spreadsheet file. Relative, absolute, and remote (http/https) paths can be 
# used.
# CONTEXT_SOURCE_FILE = ""

# EXPERIMENTAL: Path to a credentials file to authenticate with Google Drive.
# This is useful for for automated deployment. This option may be replaced by
# command line flag or environment variable. Take care not to commit or publish
# your credentials file.
# CREDENTIALS_PATH = ""

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    
    #"production": "",
    #"staging": "",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'built-with-tarbell',
    'title': 'Built With Tarbell'
}