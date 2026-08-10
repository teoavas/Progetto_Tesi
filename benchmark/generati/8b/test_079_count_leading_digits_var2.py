from funzione import count_leading_digits_var2

def test_count_leading_digits_var2_1():
    assert count_leading_digits_var2([1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]

def test_count_leading_digits_var2_2():
    assert count_leading_digits_var2([1, 1, 1, 1, 1]) == [5, 1, 1, 1, 1, 1, 1, 1, 1]

def test_count_leading_digits_var2_3():
    assert count_leading_digits_var2([2, 2, 2, 2, 2]) == [1, 5, 1, 1, 1, 1, 1, 1, 1]

def test_count_leading_digits_var2_4():
    assert count_leading_digits_var2([3, 3, 3, 3, 3]) == [1, 1, 5, 1, 1, 1, 1, 1, 1]

def test_count_leading_digits_var2_5():
    assert count_leading_digits_var2([4, 4, 4, 4, 4]) == [1, 1, 1, 5, 1, 1, 1, 1, 1]

def test_count_leading_digits_var2_6():
    assert count_leading_digits_var2([5, 5, 5, 5, 5]) == [1, 1, 1, 1, 5, 1, 1, 1, 1]

def test_count_leading_digits_var2_7():
    assert count_leading_digits_var2([6, 6, 6, 6, 6]) == [1, 1, 1, 1, 1, 5, 1, 1, 1]

def test_count_leading_digits_var2_8():
    assert count_leading_digits_var2([7, 7, 7, 7, 7]) == [1, 1, 1, 1, 1, 1, 5, 1, 1]

def test_count_leading_digits_var2_9():
    assert count_leading_digits_var2([8, 8, 8, 8, 8]) == [1, 1, 1, 1, 1, 1, 1, 5, 1]

def test_count_leading_digits_var2_10():
    assert count_leading_digits_var2([9, 9, 9, 9, 9]) == [1, 1, 1, 1, 1, 1, 1, 1, 5]
