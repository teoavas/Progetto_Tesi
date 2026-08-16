from funzione import next_holiday

def test_next_holiday_1():
    assert next_holiday(2024, 12, 25) == ['new year\'s day', 0]

def test_next_holiday_2():
    assert next_holiday(2024, 12, 26) == ['boxing day', 1]

def test_next_holiday_3():
    assert next_holiday(2024, 11, 25) == ['christmas day', 0]

def test_next_holiday_4():
    assert next_holiday(2024, 10, 12) == ['thanksgiving day', 0]

def test_next_holiday_5():
    assert next_holiday(2024, 9, 7) == ['labour day', 0]

def test_next_holiday_6():
    assert next_holiday(2024, 8, 3) == ['civic holiday', 0]

def test_next_holiday_7():
    assert next_holiday(2024, 7, 1) == ['civic holiday', 2]
