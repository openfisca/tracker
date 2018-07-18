# -*- coding: utf-8 -*-
from openfisca_tracker.piwik import PiwikTracker, BUFFER_SIZE

TRACKER_URL = 'https://stats.data.gouv.fr/piwik.php'
TRACKER_IDSITE = 4
TRACKER_AUTH = ""

FAKE_ACTION_URL = 'https://test-tracking.openfisca.fr'
FAKE_ACTION_IP = '111.11.1.1'


tracker = PiwikTracker(TRACKER_URL, TRACKER_IDSITE, TRACKER_AUTH)


# Doesn't check that the action was actually tracked, just that it doesn't crash.
# You can manually check online at TRACKER_URL that the action was indeed tracked.
# This test never exits. It needs no be manually exited (ctrl + c).
# It might be caused by the timer thread in the piwik.py file.
def test_track():
    for i in range(BUFFER_SIZE):
        tracker.track(FAKE_ACTION_URL + '/test_track', TRACKER_AUTH)
