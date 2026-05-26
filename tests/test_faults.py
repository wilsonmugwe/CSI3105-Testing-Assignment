from logic.Calendar import Calendar
from logic.Meeting import Meeting


# -----------------------------
# KNOWN FAULT TESTS
# -----------------------------
# These tests target known defects in the system.
# The inputs used here are logically valid, but the system behaves incorrectly due to flaws in validation logic.


# Test for February 29 (leap year scenario)
# The system pre-populates invalid entries for February 29, which leads to incorrect behaviour.
# This test verifies that an additional meeting can still be added, exposing the inconsistency in how the system handles this date.
def test_feb_29_bug():
    cal = Calendar()
    m = Meeting(2, 29, 9, 10)  # Valid leap day input

    cal.add_meeting(m)

    # The calendar already contains a fake "Day does not exist" entry, so the length becomes greater than 1, revealing the defect.
    assert len(cal.occupied[2][29]) > 1


# Test for November 30
# November 30 is a valid date, but the system incorrectly treats it as invalid.
# This test confirms inconsistent handling of valid dates.
def test_nov_30_bug():
    cal = Calendar()
    m = Meeting(11, 30, 9, 10)  # Valid date

    cal.add_meeting(m)

    # Similar to February, the presence of pre-filled invalid entries
    # results in unexpected behaviour.
    assert len(cal.occupied[11][30]) > 1


# Test for December (month = 12)
# December is a valid month, but due to incorrect validation logic,the system rejects it (m_month >= 12 condition).
# This test is expected to fail, demonstrating the defect.
def test_december_bug():
    cal = Calendar()
    m = Meeting(12, 10, 9, 10)  # Valid month

    # This should succeed, but raises an exception due to faulty condition
    cal.add_meeting(m)


# Test for 11 PM (hour = 23)
# 23 is a valid hour, but the system incorrectly rejects it due to the condition (m_start >= 23).
# This test exposes the boundary error in time validation.
def test_11pm_bug():
    cal = Calendar()
    m = Meeting(5, 10, 23, 23)  # Valid time

    # This should succeed, but raises an exception due to faulty validation
    cal.add_meeting(m)