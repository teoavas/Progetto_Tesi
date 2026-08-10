from funzione import find_adjacent_product

def test_find_adjacent_product_1():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    assert find_adjacent_product(N, data) == 9

def test_find_adjacent_product_2():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 2
    assert find_adjacent_product(N, data) == 36

def test_find_adjacent_product_3():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 3
    assert find_adjacent_product(N, data) == 36

def test_find_adjacent_product_4():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 4
    assert find_adjacent_product(N, data) == 36

def test_find_adjacent_product_5():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 5
    assert find_adjacent_product(N, data) == 36

def test_find_adjacent_product_6():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 0
    assert find_adjacent_product(N, data) == 9

def test_find_adjacent_product_7():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    assert find_adjacent_product(N, data) == 9

def test_find_adjacent_product_8():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    assert find_adjacent_product(N, data) == 9
