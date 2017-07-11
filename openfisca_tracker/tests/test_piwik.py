# -*- coding: utf-8 -*-

import time

from nose.tools import assert_equal, assert_true

from tracker.piwik import *


# Doesn't check that the action was actually tracked, just that it doesn't crash. You can manually check online at PIWIK_URL that the action was indeed tracked.
def test_track():
    thread = track('https://api.openfisca.fr')


def test_track_callback():
    log = []
    def callback(response):
        log.append('callback')

    track('https://api.openfisca.fr', callback = callback)
    log.append('main')

    assert_equal(log[0], 'main')
    time.sleep(0.1)
    assert_equal(log[1], 'callback')
