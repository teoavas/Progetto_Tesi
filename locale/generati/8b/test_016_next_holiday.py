from funzione import next_holiday

def test_next_holiday_1():
    result = next_holiday(2022, 1, 17)
    assert result[0] == "family day"
    assert result[1] == 3

def test_next_holiday_2():
    result = next_holiday(2024, 2, 29)
    assert result[0] == "good friday"
    assert result[1] == 31 + 10

def test_next_holiday_3():
    result = next_holiday(2023, 3, 10)
    assert result[0] == "good friday"
    assert result[1] == 10

def test_next_holiday_4():
    result = next_holiday(2022, 4, 9)
    assert result[0] == "victoria day"
    assert result[1] == 18 - 9

def test_next_holiday_5():
    result = next_holiday(2023, 5, 17)
    assert result[0] == "canada day"
    assert result[1] == (31 - 17) + 30 + 1

def test_next_holiday_6():
    result = next_holiday(2022, 6, 1)
    assert result[0] == "canada day"
    assert result[1] == (30 - 1) + 1

def test_next_holiday_7():
    result = next_holiday(2023, 7, 4)
    assert result[0] == "civic holiday"
    assert result[1] == (31 - 4) + 3
