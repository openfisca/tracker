"""Piwik tracker tests."""

import pytest

from openfisca_tracker.piwik import BUFFER_SIZE, PiwikTracker


TRACKER_URL = "https://stats.data.gouv.fr/piwik.php"
TRACKER_IDSITE = 4
TRACKER_AUTH = ""

FAKE_ACTION_URL = "https://test-tracking.openfisca.fr"
FAKE_ACTION_IP = "111.11.1.1"


class TestPiwikTracker(PiwikTracker):
    """Dummy Piwik tracker."""

    __test__ = False

    def start_timer(self):
        """Do nothing."""

    def stop_timer(self):
        """Do nothing."""


@pytest.fixture(name = "tracker")
def create_tracker():
    """Fixture to create a tracker."""
    return TestPiwikTracker(TRACKER_URL, TRACKER_IDSITE, TRACKER_AUTH)


def test_track(tracker):
    """Test that the tracker works.

    You can manually check online at TRACKER_URL that the action was
    indeedtracked.
    """
    for i in range(BUFFER_SIZE):
        tracker.track(
            FAKE_ACTION_URL + "/test_track",
            FAKE_ACTION_IP,
            "test_country_package",
            f"/test_action_{i}",
            )

    assert len(tracker.requests) == 0
