# -*- coding: utf-8 -*-

from threading import Lock, Timer

import requests
import logging

log = logging.getLogger('gunicorn.error')
BUFFER_SIZE = 30  # We send the tracked requests by group
TIMER_INTERVAL = 3600  # We send the tracked requests every TIMER_INTERVAL seconds


class PiwikTracker:
    def __init__(self, url, idsite, token_auth):
        self.url = url  # Piwik tracking http api endpoint
        self.idsite = idsite  # Piwik id of the tracked website
        self.token_auth = token_auth
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
            requests.post(
                self.url,
                json={"requests": self.requests, "token_auth": self.token_auth},
                )
            self.requests = []

    def track(self, action_url, action_ip=""):
        tracked_request = "?idsite={}&url={}&cip={}&rec=1".format(self.idsite, action_url, action_ip)
        with self.lock:
            self.requests.append(tracked_request)
        if len(self.requests) == BUFFER_SIZE:
            self.send()
