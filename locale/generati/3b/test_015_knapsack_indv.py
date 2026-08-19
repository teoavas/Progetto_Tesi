from funzione import knapsack_indv

def test_knapsack_indv_1():
    assert knapsack_indv(3, [10, 20, 30], [5, 10, 15], 25) == [2]

def test_knapsack_indv_2():
    assert knapsack_indv(4, [100, 200, 300, 400], [50, 150, 250, 350], 500) == [3, 0]

def test_knapsack_indv_3():
    with pytest.raises(ValueError):
        knapsack_indv(5, [10, 20, 30], [5, 10, 15], -1)

def test_knapsack_indv_4():
    assert knapsack_indv(2, [100, 200], [50, 150], 300) == []

def test_knapsack_indv_5():
    assert knapsack_indv(3, [10, 20, 30], [5, 10, 15], 0) == []

def test_knapsack_indv_6():
    with pytest.raises(TypeError):
        knapsack_indv(4, 'a', [50, 150], 500)

def test_knapsack_indv_7():
    assert knapsack_indv(5, [100, 200, 300, 400, 500], [50, 150, 250, 350, 450], 600) == [4]
