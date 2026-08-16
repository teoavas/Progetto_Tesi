import pytest

def test_next_holiday_1():
    result = next_holiday(2022, 12, 25)
    assert isinstance(result, list), "Expected a list of holidays"
    assert len(result) > 0, "Expected at least one holiday"

test_next_holiday_2.py
