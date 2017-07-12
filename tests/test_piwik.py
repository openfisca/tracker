# -*- coding: utf-8 -*-

import time

from nose.tools import assert_equal

from openfisca_tracker.piwik import PiwikTracker

TRACKER_URL = 'https://openfisca.innocraft.cloud/piwik.php'
TRACKER_IDSITE = 1
FAKE_ACTION_URL = 'https://test-tracking.openfisca.fr'


tracker = PiwikTracker(TRACKER_URL, TRACKER_IDSITE)


# Doesn't check that the action was actually tracked, just that it doesn't crash.
# You can manually check online at TRACKER_URL that the action was indeed tracked.
def test_track():
    tracker.track(FAKE_ACTION_URL + '/test_track')


def test_track_callback():
    log = []

    def callback(response):
        log.append('callback')

    tracker.track(FAKE_ACTION_URL + '/test_track_callback', callback = callback)
    log.append('main')

    assert_equal(log[0], 'main')
    time.sleep(0.2)
    assert_equal(log[1], 'callback')
