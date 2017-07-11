# -*- coding: utf-8 -*-

import os
import pkg_resources

import logging
import ConfigParser

from urllib import urlencode
from urlparse import urljoin

from unirest import post

# TODO: Bulk tracking (from flask import jsonify)
# {
#    "requests": [
#       "?idsite=1&url=http://example.org&action_name=Test bulk log Pageview&rec=1",
#       "?idsite=1&url=http://example.net/test.htm&action_name=Another bul k page view&rec=1"
#    ],
#    "token_auth": "33dc3f2536d3025974cccb4b4d2d98f4"
# }

CONF_FILE_NAME = 'config/config.ini'
log = logging.getLogger(__name__)

# TODO: Clean? application = None
# TODO: Clean? urls = []

# Piwik parameters:

URL="https://openfisca.innocraft.cloud/piwik.php"
idsite=1
rec=1

# TODO: Use action_name to create a category/api version number?
# TODO: Track unique visitors with _id?

def new_piwik_url(url):  # The full URL for the current action.
    params = urlencode(get_piwik_params(ur))
    return u'https://openfisca.innocraft.cloud/piwik.php?' + params

def get_piwik_params(url):
    return {'idsite': idsite, 'rec': rec, 'url': url }

# In case of timeout or any other exception during the connection of the request:
def exception_handler(request, exception):
    log.error("Request failed")

def track(action_url, callback=None):
    post(URL, params=get_piwik_params(action_url), callback=callback)
