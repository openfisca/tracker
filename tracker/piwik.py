# -*- coding: utf-8 -*-

import logging
import ConfigParser

from urllib import urlencode
from urlparse import urljoin

import grequests

# TODO: Bulk tracking (from flask import jsonify)
# {
#    "requests": [
#       "?idsite=1&url=http://example.org&action_name=Test bulk log Pageview&rec=1",
#       "?idsite=1&url=http://example.net/test.htm&action_name=Another bul k page view&rec=1"
#    ],
#    "token_auth": "33dc3f2536d3025974cccb4b4d2d98f4"
# }

CONF_FILE_NAME = 'config/config.ini'
raw_config_parser = None
log = logging.getLogger(__name__)

# TODO: Clean? application = None
# TODO: Clean? urls = []

# Piwik parameters:


idsite=1
rec=1

# TODO: Use action_name to create a category/api version number?
# TODO: Track unique visitors with _id?

def get_raw_config_parser():
    if not raw_config_parser:
        pkg_root_dir = pkg_resources.get_distribution('Tracker').location
        conf_file_path = os.path.join(pkg_root_dir, CONF_FILE_NAME)

        config = ConfigParser.RawConfigParser()
        raw_config_parser = config.read(conf_file_path)
    return raw_config_parser

def new_piwik_url(url):  # The full URL for the current action.
    params = urlencode({'idsite': idsite, 'rec': rec, 'url': url })
    return u'https://openfisca.innocraft.cloud/piwik.php?' + params


def set_requests(urls):
    return (grequests.get(u) for u in urls)


def set_timedout_requests(urls, timeout):
    return (grequests.get(u, timeout=timeout) for u in urls)


def send_all(requests):
    grequests.map(requests)


def send_all_and_handle(requests, exception_handler):
    grequests.map(requests, exception_handler=exception_handler)


# In case of timeout or any other exception during the connection of the request:
def exception_handler(request, exception):
    log.error("Request failed")


def track(urls):
    requests = set_requests(urls)
    send_all(requests, exception_handler)
