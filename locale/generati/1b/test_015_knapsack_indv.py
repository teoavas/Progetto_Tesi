test_knapsack_indv_1
def test_knapsack_indv_2():
    assert knapsack_indv(3, [10, 20, 30], [5, 15, 25], 50) == [0, 1, 2]
test_knapsack_indv_3
def test_knapsack_indv_4():
    assert knapsack_indv(4, [100, 200, 300, 400], [10, 20, 30, 40], 50) == [0, 1, 2, 3]
test_knapsack_indv_5
def test_knapsack_indv_6():
    assert knapsack_indv(5, [500, 600, 700, 800, 900], [15, 25, 35, 45, 55], 50) == [0, 1, 2, 3, 4]
test_knapsack_indv_7
def test_knapsack_indv_8():
    assert knapsack_indv(6, [1000, 1200, 1400, 1600, 1800, 2000], [20, 30, 40, 50, 60, 70], 50) == [0, 1, 2, 3, 4, 5]
