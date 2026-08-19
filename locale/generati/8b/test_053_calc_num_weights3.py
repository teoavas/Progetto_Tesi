from funzione import calc_num_weights3

def test_calc_num_weights3_1():
    assert calc_num_weights3(10, [20], 5, [True], [False]) == 205

def test_calc_num_weights3_2():
    assert calc_num_weights3(10, [], 5, [True], [True]) == 50

def test_calc_num_weights3_3():
    assert calc_num_weights3(10, [20, 30], 5, [True, True], [False, False]) == 2050

def test_calc_num_weights3_4():
    assert calc_num_weights3(10, [20, 30], 5, [True, False], [False, True]) == 130

def test_calc_num_weights3_5():
    assert calc_num_weights3(10, [], 5, [False], [True]) == 5

def test_calc_num_weights3_6():
    assert calc_num_weights3(10, [20], 5, [False], [False]) == 0

def test_calc_num_weights3_7():
    assert calc_num_weights3(10, [], 5, [True], [False]) == 50
