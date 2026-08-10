from funzione import knapsack_indv

def test_knapsack_indv_1():
    n = 3
    c = [10, 20, 30]
    w = [5, 10, 15]
    W = 20
    assert knapsack_indv(n, c, w, W) == [1, 3]

def test_knapsack_indv_2():
    n = 2
    c = [10, 20]
    w = [5, 10]
    W = 15
    assert knapsack_indv(n, c, w, W) == [1, 2]

def test_knapsack_indv_3():
    n = 1
    c = [10]
    w = [5]
    W = 5
    assert knapsack_indv(n, c, w, W) == [1]

def test_knapsack_indv_4():
    n = 4
    c = [10, 20, 30, 40]
    w = [5, 10, 15, 20]
    W = 30
    assert knapsack_indv(n, c, w, W) == [1, 3]

def test_knapsack_indv_5():
    n = 5
    c = [10, 20, 30, 40, 50]
    w = [5, 10, 15, 20, 25]
    W = 40
    assert knapsack_indv(n, c, w, W) == [1, 2, 4]

def test_knapsack_indv_6():
    n = 0
    c = []
    w = []
    W = 0
    assert knapsack_indv(n, c, w, W) == []

def test_knapsack_indv_7():
    n = 1
    c = [10]
    w = [5]
    W = 0
    assert knapsack_indv(n, c, w, W) == []
