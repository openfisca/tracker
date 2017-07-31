# -*- coding: utf-8 -*-

import json
from threading import Lock, Timer

from unirest import post

BUFFER_SIZE = 30  # We send the tracked requests by group
TIMER_INTERVAL = 3600  # We send the tracked requests every TIMER_INTERVAL seconds


def default_callback(response):
    return


class PiwikTracker:
    def __init__(self, url, idsite):
        self.url = url  # Piwik tracking http api endpoint
        self.idsite = idsite  # Piwik id of the tracked website
        self.requests = []  # Awaiting tracked requests
        self.lock = Lock()
        self.start_timer()

    def start_timer(self):
        Timer(TIMER_INTERVAL, self.stop_timer).start()

    def stop_timer(self):
        if self.requests:
            self.send()
        self.start_timer()

    def send(self):
        with self.lock:
            post(
                self.url,
                headers = { "Accept": "application/json" },
                params = json.dumps({"requests": self.requests}),
                callback = default_callback
                )
            self.requests = []

    def track(self, action_url):
        tracked_request = "?idsite={}&url={}&rec=1".format(self.idsite, action_url)
        with self.lock:
            self.requests.append(tracked_request)
        if len(self.requests) == BUFFER_SIZE:
            self.send()
