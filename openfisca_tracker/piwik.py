# -*- coding: utf-8 -*-

from urllib import urlencode
from unirest import post


class PiwikTracker:

    url = None  # Piwik tracking http api endpoint. 
    idsite = None  # Piwik id of the tracked website.

    def __init__(self, url, idsite):
        self.url = url
        self.idsite = idsite

    def track(self, action_url, callback = None):
        params = {'idsite': self.idsite, 'rec': 1, 'url': action_url }
        post(self.url, params = params, callback = callback)
