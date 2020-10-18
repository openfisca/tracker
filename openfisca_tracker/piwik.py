"""
OpenFisca Piwik Tracker.

It allows for usage analytics on a [Piwik](https://piwik.org) analytics
plateform.
"""

import logging
from threading import Lock, Timer

import grequests

log = logging.getLogger('gunicorn.error')

# We send the tracked requests by group
BUFFER_SIZE = 30

# We send the tracked requests every TIMER_INTERVAL seconds
TIMER_INTERVAL = 3600


class PiwikTracker:
    """
    PiwikTracker.

    It seems that each of the gunicorn worker created by `openfisca serve`
    creates a separate tracker object.
    """

    def __init__(self, url, idsite, token_auth):
        self.url = url  # Piwik tracking http api endpoint
        self.idsite = idsite  # Piwik id of the tracked website
        self.token_auth = token_auth
        self.requests = []  # Awaiting tracked requests
        self.lock = Lock()
        self.start_timer()

    def start_timer(self):
        """
        Start the timer.

        It runs for TIMER_INTERVAL seconds and then calls
        `self.stop_timer`.
        """
        Timer(TIMER_INTERVAL, self.stop_timer).start()

    def stop_timer(self):
        """
        Restart the timer.

        If there are any requests, it sends them.
        """
        if self.requests:
            self.send()

        self.start_timer()

    def send(self):
        """
        Send tracked requests.

        It locks in case the Timer and Buffer trigger `send` simultaneously.
        It logs failed requests.
        """

        def exception_handler(request, exception):
            logging.warning("Tracker request failed : {}".format(exception))

        with self.lock:
            req = grequests.post(
                self.url,
                json = {
                    "requests": self.requests,
                    "token_auth": self.token_auth,
                    },
                )
            grequests.map([req], exception_handler=exception_handler)
            self.requests = []

    def track(
            self,
            action_url,
            action_ip = "",
            api_version = "unknown_version",
            action = "unknown_action",
            ):
        """
        Track a request.

        It locks in case `send` and `track` try to access `self.requests`
        simultaneously.

        It sends the requests to track once they have the BUFFER_SIZE.
        """
        tracked_request = "?idsite={}&url={}&cip={}&e_c={}&e_a={}&rec=1"
        tracked_request = tracked_request.format(
            self.idsite, action_url, action_ip, api_version, action,
            )

        with self.lock:
            self.requests.append(tracked_request)

        if len(self.requests) == BUFFER_SIZE:
            self.send()
