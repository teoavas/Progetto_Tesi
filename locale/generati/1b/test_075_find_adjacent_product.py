import pytest

def test_find_adjacent_product_1():
    data = [[2, 3], [4, 5]]
    expected = 120
    assert find_adjacent_product(2, data) == expected

def test_find_adjacent_product_2():
    data = [[10, 20], [30, 40]]
    expected = 2000
    assert find_adjacent_product(1, data) == expected

def test_find_adjacent_product_3():
    data = [[5, 6], [7, 8]]
    expected = 210
    assert find_adjacent_product(2, data) == expected

def test_find_adjacent_product_4():
    data = [[9, 10], [11, 12]]
    expected = 1800
    assert find_adjacent_product(1, data) == expected

def test_find_adjacent_product_5():
    data = [[8, 7], [6, 5]]
    expected = 280
    assert find_adjacent_product(2, data) == expected

def test_find_adjacent_product_6():
    data = [[4, 3], [2, 1]]
    expected = 12
    assert find_adjacent_product(1, data) == expected

def test_find_adjacent_product_7():
    data = [[9, 8], [7, 6]]
    expected = 504
    assert find_adjacent_product(2, data) == expected

def test_find_adjacent_product_8():
    data = [[5, 4], [3, 2]]
    expected = 20
    assert find_adjacent_product(1, data) == expected
