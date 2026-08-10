from funzione import time_in_swiss_german

def test_time_in_swiss_german_1():
    assert time_in_swiss_german(0, 0) == "12 i znacht"

def test_time_in_swiss_german_2():
    assert time_in_swiss_german(6, 0) == "6 i am morge"

def test_time_in_swiss_german_3():
    assert time_in_swiss_german(12, 0) == "12 i am mittag"

def test_time_in_swiss_german_4():
    assert time_in_swiss_german(12, 15) == "viertel ab 12 i am mittag"

def test_time_in_swiss_german_5():
    assert time_in_swiss_german(12, 30) == "halbi 12 i am mittag"

def test_time_in_swiss_german_6():
    assert time_in_swiss_german(12, 45) == "viertel vor 12 i am mittag"

def test_time_in_swiss_german_7():
    assert time_in_swiss_german(13, 0) == "1 i am namittag"

def test_time_in_swiss_german_8():
    assert time_in_swiss_german(23, 59) == "21 i znacht"
