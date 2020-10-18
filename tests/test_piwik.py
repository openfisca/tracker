# -*- coding: utf-8 -*-
from openfisca_tracker.piwik import PiwikTracker, BUFFER_SIZE
import pytest

TRACKER_URL = 'https://stats.data.gouv.fr/piwik.php'
TRACKER_IDSITE = 4
TRACKER_AUTH = ""

FAKE_ACTION_URL = 'https://test-tracking.openfisca.fr'
FAKE_ACTION_IP = '111.11.1.1'


class TestPiwikTracker(PiwikTracker):
    def __init__(self, url, idsite, token_auth):
        super().__init__(url, idsite, token_auth)

    def start_timer(self):
        pass

    def stop_timer(self):
        pass


@pytest.fixture
def tracker():
    tracker = TestPiwikTracker(TRACKER_URL, TRACKER_IDSITE, TRACKER_AUTH)
    yield tracker


# You can manually check online at TRACKER_URL that the action was indeed tracked.
def test_track(tracker):
    for i in range(BUFFER_SIZE):
        tracker.track(FAKE_ACTION_URL + '/test_track', FAKE_ACTION_IP, "test_country_package", f"/test_action_{i}")

    assert len(tracker.requests) == 0
