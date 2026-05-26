import pytest
from logic.Calendar import Calendar
from logic.Meeting import Meeting
from logic.ConflictException import ConflictsException


# -----------------------------
# MONTH BOUNDARY TESTS
# -----------------------------
# These tests evaluate values at and around the valid month range (1–12).

# Lower boundary (valid): month = 1
# This should be accepted as it is the minimum valid month.
def test_month_boundary_low_valid():
    cal = Calendar()
    m = Meeting(1, 10, 9, 10)

    cal.add_meeting(m)

    # Verify meeting is successfully stored
    assert cal.get_meeting(1, 10, 0) == m


# Upper boundary (valid): month = 12
# This should be valid, but due to a bug in the system (>= 12 condition),it is incorrectly rejected.
def test_month_boundary_high_valid():
    cal = Calendar()
    m = Meeting(12, 10, 9, 10)

    # Expected: should succeed
    # Actual: fails due to incorrect validation logic
    cal.add_meeting(m)

    assert cal.get_meeting(12, 10, 0) == m


# Lower boundary (invalid): month = 0
# This is below the valid range and should be rejected.
def test_month_boundary_low_invalid():
    cal = Calendar()
    m = Meeting(0, 10, 9, 10)

    # Expect an exception for invalid month
    with pytest.raises(ConflictsException):
        cal.add_meeting(m)


# -----------------------------
# DAY BOUNDARY TESTS
# -----------------------------
# These tests evaluate the upper limit of valid days.

# Upper boundary (invalid): day = 31
# The system incorrectly restricts valid days to <= 30, so day 31 is rejected even though some months allow it.
def test_day_boundary_high_invalid():
    cal = Calendar()
    m = Meeting(5, 31, 9, 10)

    # Expect an exception due to system limitation
    with pytest.raises(ConflictsException):
        cal.add_meeting(m)


# -----------------------------
# TIME BOUNDARY TESTS
# -----------------------------
# These tests evaluate the valid time range (0–23).

# Boundary case: start = 0 (minimum), end = 23 (maximum)
# This should represent a full valid time range within a day.
def test_hour_boundary_valid():
    cal = Calendar()
    m = Meeting(5, 10, 0, 23)

    cal.add_meeting(m)

    # Verify meeting is correctly added
    assert cal.get_meeting(5, 10, 0) == m