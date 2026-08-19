from funzione import count_leading_digits_var2

def test_count_leading_digits_var2_1():
    assert count_leading_digits_var2([1, 2, 3]) == [1, 1, 1, 0, 0, 0, 0, 0, 0]

def test_count_leading_digits_var2_2():
    assert count_leading_digits_var2([4, 5, 6]) == [0, 0, 0, 1, 1, 1, 0, 0, 0]

def test_count_leading_digits_var2_3():
    assert count_leading_digits_var2([7, 8, 9]) == [0, 0, 0, 0, 0, 0, 1, 1, 1]

def test_count_leading_digits_var2_4():
    assert count_leading_digits_var2([1, 1, 1, 1, 1, 1]) == [5, 0, 0, 0, 0, 0, 0, 0, 0]

def test_count_leading_digits_var2_5():
    assert count_leading_digits_var2([2, 3, 4, 5, 6, 7]) == [1, 1, 1, 1, 1, 1, 0, 0, 0]

def test_count_leading_digits_var2_6():
    assert count_leading_digits_var2([9, 8, 7, 6, 5, 4]) == [0, 0, 0, 0, 0, 0, 1, 1, 1]

def test_count_leading_digits_var2_7():
    assert count_leading_digits_var2([]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
