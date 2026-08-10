from funzione import next_holiday

def test_next_holiday_1():
    assert next_holiday(2024, 1, 1) == ['family day', 17]

def test_next_holiday_2():
    assert next_holiday(2024, 2, 29) == ['good friday', 31 + 10]

def test_next_holiday_3():
    assert next_holiday(2024, 3, 1) == ['good friday', 10]

def test_next_holiday_4():
    assert next_holiday(2024, 4, 1) == ['good friday', 10]

def test_next_holiday_5():
    assert next_holiday(2024, 4, 10) == ['victoria day', 18]

def test_next_holiday_6():
    assert next_holiday(2024, 5, 18) == ['canada day', 30 + 1]

def test_next_holiday_7():
    assert next_holiday(2024, 6, 1) == ['canada day', 1]

def test_next_holiday_8():
    assert next_holiday(2024, 7, 1) == ['civic holiday', 3]

def test_next_holiday_9():
    assert next_holiday(2024, 8, 1) == ['civic holiday', 3]

def test_next_holiday_10():
    assert next_holiday(2024, 9, 1) == ['labour day', 7]

def test_next_holiday_11():
    assert next_holiday(2024, 9, 7) == ['thanksgiving day', 12]

def test_next_holiday_12():
    assert next_holiday(2024, 10, 1) == ['thanksgiving day', 12]

def test_next_holiday_13():
    assert next_holiday(2024, 10, 12) == ['christmas day', 30 + 25]

def test_next_holiday_14():
    assert next_holiday(2024, 11, 1) == ['christmas day', 25]

def test_next_holiday_15():
    assert next_holiday(2024, 12, 1) == ['christmas day', 25]

def test_next_holiday_16():
    assert next_holiday(2024, 12, 25) == ['boxing day', 26 - 25]

def test_next_holiday_17():
    assert next_holiday(2024, 12, 26) == ['new year\'s day', 1]

def test_next_holiday_invalid_day():
    assert next_holiday(2024, 1, 32) == ['invalid day', -1]

def test_next_holiday_invalid_month():
    assert next_holiday(2024, 13, 1) == ['invalid month', -1]
