import pytest
from logic.Calendar import Calendar
from logic.ConflictException import ConflictsException


def test_month_lower_boundary():
    Calendar.check_times(1, 15, 10, 11)


def test_month_upper_boundary_should_fail():
    with pytest.raises(ConflictsException):
        Calendar.check_times(12, 15, 10, 11)


def test_day_lower_boundary():
    Calendar.check_times(5, 1, 10, 11)


def test_day_upper_boundary_should_fail():
    with pytest.raises(ConflictsException):
        Calendar.check_times(5, 31, 10, 11)


def test_hour_lower_boundary():
    Calendar.check_times(5, 15, 0, 1)


def test_hour_upper_boundary_should_fail():
    with pytest.raises(ConflictsException):
        Calendar.check_times(5, 15, 23, 23)