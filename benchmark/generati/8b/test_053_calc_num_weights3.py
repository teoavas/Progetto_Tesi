from funzione import calc_num_weights3

def test_calc_num_weights3_1():
    assert calc_num_weights3(5, [], False, False, False) == 0

def test_calc_num_weights3_2():
    assert calc_num_weights3(5, [10], False, False, False) == 50

def test_calc_num_weights3_3():
    assert calc_num_weights3(5, [10], True, False, False) == 55

def test_calc_num_weights3_4():
    assert calc_num_weights3(5, [10, 20], False, False, False) == 200

def test_calc_num_weights3_5():
    assert calc_num_weights3(5, [10, 20], True, False, False) == 210

def test_calc_num_weights3_6():
    assert calc_num_weights3(5, [10, 20], True, True, False) == 220

def test_calc_num_weights3_7():
    assert calc_num_weights3(5, [10, 20, 30], False, False, False) == 600

def test_calc_num_weights3_8():
    assert calc_num_weights3(5, [10, 20, 30], True, True, True) == 630
