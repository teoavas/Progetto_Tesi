```python
from funzione import find_adjacent_product

def test_find_adjacent_product_1():
    data = [[1, 2], [3, 4]]
    N = 1
    assert find_adjacent_product(N, data) == 8

def test_find_adjacent_product_2():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 2
    assert find_adjacent_product(N, data) == 504

def test_find_adjacent_product_3():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 0
    assert find_adjacent_product(N, data) == 9

def test_find_adjacent_product_4():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = -1
    assert find_adjacent_product(N, data) == 9

def test_find_adjacent_product_5():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 10
    assert find_adjacent_product(N, data) == 9

def test_find_adjacent_product_6():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    data[0][0] = 10
    assert find_adjacent_product(N, data) == 40

def test_find_adjacent_product_7():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    data[0][1] = 10
    assert find_adjacent_product(N, data) == 40

def test_find_adjacent_product_8():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    data[0][2] = 10
    assert find_adjacent_product(N, data) == 40

def test_find_adjacent_product_9():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    data[1][0] = 10
    assert find_adjacent_product(N, data) == 40

def test_find_adjacent_product_10():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    data[1][1] = 10
    assert find_adjacent_product(N, data) == 40

def test_find_adjacent_product_11():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    data[1][2] = 10
    assert find_adjacent_product(N, data) == 40

def test_find_adjacent_product_12():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    data[2][0] = 10
    assert find_adjacent_product(N, data) == 40

def test_find_adjacent_product_13():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    data[2][1] = 10
    assert find_adjacent_product(N, data) == 40

def test_find_adjacent_product_14():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    data[2][2] = 10
    assert find_adjacent_product(N, data) == 40

def test_find_adjacent_product_15():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    data[0][0] = 10
    data[1][1] = 10
    assert find_adjacent_product(N, data) == 100

def test_find_adjacent_product_16():
    data = [[1, 2, 3],
