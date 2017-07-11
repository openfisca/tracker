# -*- coding: utf-8 -*-

import grequests
import logging

# TODO: Bulk tracking
# {
#    "requests": [
#       "?idsite=1&url=http://example.org&action_name=Test bulk log Pageview&rec=1",
#       "?idsite=1&url=http://example.net/test.htm&action_name=Another bul k page view&rec=1"
#    ],
#    "token_auth": "33dc3f2536d3025974cccb4b4d2d98f4"
# }

log = logging.getLogger(__name__)
urls = []

# The ID of the website we're tracking.
idsite = ""
# Required for tracking.
rec = 1
# The full URL for the current action.
url = ""
# Piwik api version
apiv = 1
# The full HTTP Referrer URL.
urlref = ""

# TODO: Use action_name to create a category/api version number?
# TODO: Track unique visitors with _id?


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
