import pytest

def test_time_in_swiss_german_1():
    assert time_in_swiss_german(5, 0) == "15 am mittag"

def test_time_in_swiss_german_2():
    assert time_in_swiss_german(12, 30) == "18 abig"

def test_time_in_swiss_german_3():
    assert time_in_swiss_german(9, 45) == "54 halbi"

def test_time_in_swiss_german_4():
    assert time_in_swiss_german(15, 0) == "15 viertel ab"

def test_time_in_swiss_german_5():
    assert time_in_swiss_german(18, 30) == "21 halbi"

def test_time_in_swiss_german_6():
    assert time_in_swiss_german(0, 45) == "15 viertel vor"

def test_time_in_swiss_german_7():
    assert time_in_swiss_german(12, 60) == "18 abig"

def test_time_in_swiss_german_8():
    assert time_in_swiss_german(9, 0) == "15 am mittag"
