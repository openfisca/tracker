# -*- coding: utf-8 -*-

import json

from unirest import post

BUFFER_SIZE = 10


def default_callback(response):
    return


class PiwikTracker:

    url = None  # Piwik tracking http api endpoint.
    idsite = None  # Piwik id of the tracked website.

    def __init__(self, url, idsite):
        self.url = url
        self.idsite = idsite
        self.requests = []


    def track(self, action_url):
        tracked_request = "?idsite={}&url={}&rec=1".format(self.idsite, action_url)
        self.requests.append(tracked_request)
        if len(self.requests) == BUFFER_SIZE:
            post(
                self.url,
                headers = { "Accept": "application/json" },
                params = json.dumps({"requests": self.requests}),
                callback = default_callback
                )
            self.requests = []
