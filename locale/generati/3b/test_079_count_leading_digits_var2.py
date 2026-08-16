from funzione import count_leading_digits_var2

def test_count_leading_digits_var2_1():
    assert count_leading_digits_var2(123) == [1, 0, 0, 0, 0, 0, 0, 0, 0]

def test_count_leading_digits_var2_2():
    assert count_leading_digits_var2(111) == [3, 0, 0, 0, 0, 0, 0, 0, 0]

def test_count_leading_digits_var2_3():
    assert count_leading_digits_var2(222) == [1, 2, 0, 0, 0, 0, 0, 0, 0]

def test_count_leading_digits_var2_4():
    assert count_leading_digits_var2(999) == [3, 0, 0, 0, 0, 0, 0, 0, 0]

def test_count_leading_digits_var2_5():
    assert count_leading_digits_var2(123456789) == [1, 1, 1, 1, 1, 1, 1, 1, 1]

def test_count_leading_digits_var2_6():
    assert count_leading_digits_var2(987654321) == [0, 0, 0, 0, 0, 0, 0, 0, 8]

def test_count_leading_digits_var2_7():
    assert count_leading_digits_var2(111111111) == [3, 0, 0, 0, 0, 0, 0, 0, 0]
