import pytest
from logic.Calendar import Calendar
from logic.ConflictException import ConflictsException


def test_valid_equivalence_class():
    Calendar.check_times(5, 15, 10, 11)


def test_invalid_month_low():
    with pytest.raises(ConflictsException):
        Calendar.check_times(0, 15, 10, 11)


def test_invalid_month_high():
    with pytest.raises(ConflictsException):
        Calendar.check_times(13, 15, 10, 11)


def test_invalid_day_low():
    with pytest.raises(ConflictsException):
        Calendar.check_times(5, 0, 10, 11)


def test_invalid_day_high():
    with pytest.raises(ConflictsException):
        Calendar.check_times(5, 32, 10, 11)


def test_invalid_hour():
    with pytest.raises(ConflictsException):
        Calendar.check_times(5, 15, 25, 26)