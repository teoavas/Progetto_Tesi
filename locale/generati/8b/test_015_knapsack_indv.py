from funzione import knapsack_indv

def test_knapsack_indv_1():
    n = 3
    c = [10, 20, 30]
    w = ['a', 'b', 'c']
    W = 5
    assert knapsack_indv(n, c, w, W) == [2]

def test_knapsack_indv_2():
    n = 3
    c = [10, 20, 30]
    w = ['a', 'b', 'c']
    W = 8
    assert knapsack_indv(n, c, w, W) == [1, 3]

def test_knapsack_indv_3():
    n = 2
    c = [10, 20]
    w = ['a', 'b']
    W = 5
    assert knapsack_indv(n, c, w, W) == [1]

def test_knapsack_indv_4():
    n = 3
    c = [10, 20, 30]
    w = ['a', 'b', 'c']
    W = 0
    assert knapsack_indv(n, c, w, W) == []

def test_knapsack_indv_5():
    n = 1
    c = [10]
    w = ['a']
    W = 5
    assert knapsack_indv(n, c, w, W) == [1]

def test_knapsack_indv_6():
    n = 3
    c = [10, 20, 30]
    w = ['a', 'b', 'c']
    W = -5
    assert knapsack_indv(n, c, w, W) == []

def test_knapsack_indv_7():
    n = 0
    c = []
    w = []
    W = 5
    assert knapsack_indv(n, c, w, W) == []

def test_knapsack_indv_8():
    n = 3
    c = [10, 20, 30]
    w = ['a', 'b', 'c']
    W = float('inf')
    assert knapsack_indv(n, c, w, W) == [1, 2, 3]
