from funzione import time_in_swiss_german

def test_time_in_swiss_german_1():
    assert time_in_swiss_german(0, 15) == "viertel ab 12 znacht"

def test_time_in_swiss_german_2():
    assert time_in_swiss_german(6, 30) == "halbi am morge"

def test_time_in_swiss_german_3():
    assert time_in_swiss_german(12, 0) == "12 am mittag"

def test_time_in_swiss_german_4():
    assert time_in_swiss_german(18, 45) == "viertel vor 6 am namittag"

def test_time_in_swiss_german_5():
    assert time_in_swiss_german(22, 15) == "viertel ab 10 znacht"

def test_time_in_swiss_german_6():
    assert time_in_swiss_german(23, 30) == "halbi vor 1 znacht"

def test_time_in_swiss_german_7():
    assert time_in_swiss_german(0, 45) == "viertel vor 12 znacht"
