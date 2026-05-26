import pytest
from logic.Calendar import Calendar
from logic.Meeting import Meeting
from logic.ConflictException import ConflictsException


# -----------------------------
# VALID PARTITION TEST
# -----------------------------
# This test verifies that a valid input combination (month, day, time) is accepted by the system and correctly stored in the calendar.
def test_valid_meeting():
    cal = Calendar()
    m = Meeting(5, 10, 9, 10)  # Valid meeting input

    cal.add_meeting(m)

    # Check that the meeting was successfully added
    assert cal.get_meeting(5, 10, 0) == m


# -----------------------------
# INVALID MONTH PARTITION TESTS
# -----------------------------
# These tests verify that invalid month values (outside 1–12) are correctly rejected by the system.

# Lower bound invalid month (below valid range)
def test_invalid_month_low():
    cal = Calendar()
    m = Meeting(0, 10, 9, 10)  # Invalid month

    # Expect system to raise an exception
    with pytest.raises(ConflictsException):
        cal.add_meeting(m)


# Upper bound invalid month (above valid range)
def test_invalid_month_high():
    cal = Calendar()
    m = Meeting(13, 10, 9, 10)  # Invalid month

    # Expect system to raise an exception
    with pytest.raises(ConflictsException):
        cal.add_meeting(m)


# -----------------------------
# INVALID DAY PARTITION TESTS
# -----------------------------
# These tests verify that invalid day values (outside 1–31) are correctly rejected by the system.

# Lower bound invalid day (below valid range)
def test_invalid_day_low():
    cal = Calendar()
    m = Meeting(5, 0, 9, 10)  # Invalid day

    # Expect system to raise an exception
    with pytest.raises(ConflictsException):
        cal.add_meeting(m)


# Upper bound invalid day (above valid range)
def test_invalid_day_high():
    cal = Calendar()
    m = Meeting(5, 32, 9, 10)  # Invalid day

    # Expect system to raise an exception
    with pytest.raises(ConflictsException):
        cal.add_meeting(m)