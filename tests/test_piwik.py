# -*- coding: utf-8 -*-

import time

from nose.tools import assert_equal

from openfisca_tracker.piwik import PiwikTracker, BUFFER_SIZE

TRACKER_URL = 'https://stats.data.gouv.fr/piwik.php'
TRACKER_IDSITE = 4
FAKE_ACTION_URL = 'https://test-tracking.openfisca.fr'


tracker = PiwikTracker(TRACKER_URL, TRACKER_IDSITE)


# Doesn't check that the action was actually tracked, just that it doesn't crash.
# You can manually check online at TRACKER_URL that the action was indeed tracked.
def test_track():
    for i in range(BUFFER_SIZE):
        tracker.track(FAKE_ACTION_URL + '/test_track')
