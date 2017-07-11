# -*- coding: utf-8 -*-

import time

from nose.tools import assert_equal

from openfisca_tracker.piwik import PiwikTracker

TRACKER_URL = 'https://openfisca.innocraft.cloud/piwik.php'
TRACKER_IDSITE = 1

tracker = PiwikTracker(TRACKER_URL, TRACKER_IDSITE)


# Doesn't check that the action was actually tracked, just that it doesn't crash.
# You can manually check online at TRACKER_URL that the action was indeed tracked.
def test_track():
    tracker.track('https://api-test.openfisca.fr/variables')  # thread


def test_track_callback():
    log = []

    def callback(response):
        log.append('callback')

    tracker.track('https://api.openfisca.fr', callback = callback)
    log.append('main')

    assert_equal(log[0], 'main')
    time.sleep(0.1)
    assert_equal(log[1], 'callback')
