import pytest
from logic.Calendar import Calendar
from logic.Organization import Organization
from logic.ConflictException import ConflictsException


def test_december_should_be_valid_but_fails():
    with pytest.raises(ConflictsException):
        Calendar.check_times(12, 15, 10, 11)


def test_day_31_should_be_valid_but_fails():
    with pytest.raises(ConflictsException):
        Calendar.check_times(1, 31, 10, 11)


def test_11pm_should_be_valid_but_fails():
    with pytest.raises(ConflictsException):
        Calendar.check_times(5, 15, 23, 23)


def test_feb_29_should_be_valid_but_fails():
    with pytest.raises(ConflictsException):
        Calendar.check_times(2, 29, 10, 11)


def test_case_sensitive_employee_lookup():
    org = Organization()
    with pytest.raises(Exception):
        org.get_employee("justin gardener")


def test_case_sensitive_room_lookup():
    org = Organization()
    with pytest.raises(Exception):
        org.get_room("jo18.330")