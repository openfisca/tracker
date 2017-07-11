# -*- coding: utf-8 -*-

from urllib import urlencode

from unirest import post

# Piwik parameters:

PIWIK_URL = "https://openfisca.innocraft.cloud/piwik.php"
ID_SITE = 1


# TODO: Use action_name to create a category/api version number?
def track(action_url, callback = None):
    params = {'idsite': ID_SITE, 'rec': 1, 'url': action_url }
    post(PIWIK_URL, params = params, callback = callback)
