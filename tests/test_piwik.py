"""Piwik tracker tests."""

from openfisca_tracker.piwik import BUFFER_SIZE, PiwikTracker

import pytest

TRACKER_URL = 'https://stats.data.gouv.fr/piwik.php'
TRACKER_IDSITE = 4
TRACKER_AUTH = ""

FAKE_ACTION_URL = 'https://test-tracking.openfisca.fr'
FAKE_ACTION_IP = '111.11.1.1'


class TestPiwikTracker(PiwikTracker):
    """Dummy Piwik tracker."""

    __test__ = False

    def __init__(self, url, idsite, token_auth):
        super().__init__(url, idsite, token_auth)

    def start_timer(self):
        """Do nothing."""
        pass

    def stop_timer(self):
        """Do nothing."""
        pass


@pytest.fixture
def tracker():
    """Fixture to create a tracker."""
    yield TestPiwikTracker(TRACKER_URL, TRACKER_IDSITE, TRACKER_AUTH)


def test_track(tracker):
    """Test that the tracker works.

    You can manually check online at TRACKER_URL that the action was
    indeedtracked.
    """
    for i in range(BUFFER_SIZE):
        tracker.track(
            FAKE_ACTION_URL + '/test_track',
            FAKE_ACTION_IP,
            "test_country_package",
            f"/test_action_{i}",
            )

    assert len(tracker.requests) == 0
