from funzione import find_adjacent_product

def test_find_adjacent_product_1():
    assert find_adjacent_product(2, [[1, 2], [3, 4]]) == 12

def test_find_adjacent_product_2():
    assert find_adjacent_product(1, [[5]]) == 5

def test_find_adjacent_product_3():
    assert find_adjacent_product(0, [[1, 2], [3, 4]]) == 1

def test_find_adjacent_product_4():
    assert find_adjacent_product(-1, [[1, 2], [3, 4]]) == 12

def test_find_adjacent_product_5():
    assert find_adjacent_product(2, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 14580

def test_find_adjacent_product_6():
    assert find_adjacent_product(-2, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 1

def test_find_adjacent_product_7():
    assert find_adjacent_product(0, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 14580
