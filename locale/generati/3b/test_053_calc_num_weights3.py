from funzione import calc_num_weights3

def test_calc_num_weights3_1():
    assert calc_num_weights3(10, [], 5, [True], [False]) == 15

def test_calc_num_weights3_2():
    assert calc_num_weights3(10, [20], 5, [True], [False]) == 50

def test_calc_num_weights3_3():
    assert calc_num_weights3(10, [20, 30], 5, [True, True], [False]) == 150

def test_calc_num_weights3_4():
    assert calc_num_weights3(10, [20, 30, 40], 5, [True, True, False], [False]) == 350

def test_calc_num_weights3_5():
    assert calc_num_weights3(10, [], 15, [True], [False]) == 25

def test_calc_num_weights3_6():
    assert calc_num_weights3(10, [20], 15, [True], [False]) == 50

def test_calc_num_weights3_7():
    assert calc_num_weights3(10, [20, 30], 15, [True, True], [False]) == 150
