from funzione import time_in_swiss_german

def test_time_in_swiss_german_1():
    assert time_in_swiss_german(6, 0) == "am morge"

def test_time_in_swiss_german_2():
    assert time_in_swiss_german(12, 0) == "am mittag"

def test_time_in_swiss_german_3():
    assert time_in_swiss_german(18, 30) == "am abig halbi"

def test_time_in_swiss_german_4():
    assert time_in_swiss_german(0, 15) == "12i znacht viertel ab"

def test_time_in_swiss_german_5():
    assert time_in_swiss_german(23, 45) == "znacht viertel vor"

def test_time_in_swiss_german_6():
    assert time_in_swiss_german(12, 15) == "am mittag viertel ab"

def test_time_in_swiss_german_7():
    assert time_in_swiss_german(0, 0) == "12i znacht"
