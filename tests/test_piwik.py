# -*- coding: utf-8 -*-
from openfisca_tracker.piwik import PiwikTracker, BUFFER_SIZE, TIMER_INTERVAL
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
    print("bye")
    # TIMER_INTERVAL = 0
    # tracker = None


# Doesn't check that the action was actually tracked, just that it doesn't crash.
# You can manually check online at TRACKER_URL that the action was indeed tracked.
# This test never exits. It needs no be manually exited (ctrl + c).
# It might be caused by the timer thread in the piwik.py file.

# @pytest.mark.timeout(1)
def test_track(tracker):
    for i in range(BUFFER_SIZE):
        tracker.track(FAKE_ACTION_URL + '/test_track', FAKE_ACTION_IP)
    assert len(tracker.requests) == 0


# @pytest.mark.timeout(1)
def test_track_with_api_version(tracker):
    for i in range(BUFFER_SIZE):
        tracker.track(FAKE_ACTION_URL + '/test_track', FAKE_ACTION_IP, "test_country_package")


# @pytest.mark.timeout(1)
def test_track_with_action(tracker):
    for i in range(BUFFER_SIZE):
        tracker.track(FAKE_ACTION_URL + '/test_track', FAKE_ACTION_IP, "test_country_package", "/test_action")
