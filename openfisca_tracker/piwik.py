# -*- coding: utf-8 -*-

from threading import Lock, Timer

import grequests
import logging

log = logging.getLogger('gunicorn.error')
BUFFER_SIZE = 30  # We send the tracked requests by group
TIMER_INTERVAL = 3600  # We send the tracked requests every TIMER_INTERVAL seconds


# It seems that each of the gunicorn worker created by `openfisca serve` creates a separate tracker object.
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
        def exception_handler(request, exception):
            logging.warning("Tracker request failed : {}".format(exception))

        # Lock in case the Timer and Buffer trigger `send()` simultaneously
        with self.lock:
            req = grequests.post(
                self.url,
                json={"requests": self.requests, "token_auth": self.token_auth},
                )
            grequests.map([req], exception_handler=exception_handler)
            self.requests = []

    def track(self, action_url, action_ip="", api_version="unknown_version", action="unknown_action"):
        # api_version example: openfisca-country-template-3.2.1

        tracked_request = "?idsite={}&url={}&cip={}&e_c={}&e_a={}&rec=1".format(self.idsite, action_url, action_ip, api_version, action)

        # Lock in case `send()` and `track()` try to access self.requests simultaneously
        with self.lock:
            self.requests.append(tracked_request)
        if len(self.requests) == BUFFER_SIZE:
            self.send()
