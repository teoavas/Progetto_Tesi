import pytest

def test_calc_num_weights3_1():
    assert calc_num_weights3(2, [4], 3, (True, False), (False, True)) == 8 + 12

def test_calc_num_weights3_2():
    assert calc_num_weights3(5, [], 0, (True, False), (False, True)) == 20

def test_calc_num_weights3_3():
    assert calc_num_weights3(1, [4], 0, (True, False), (False, True)) == 4 + 4

def test_calc_num_weights3_4():
    assert calc_num_weights3(2, [], 0, (True, False), (False, True)) == 8 + 12

def test_calc_num_weights3_5():
    assert calc_num_weights3(1, [4], 0, (True, False), (False, True)) == 4 + 4

def test_calc_num_weights3_6():
    assert calc_num_weights3(2, [], 0, (True, False), (False, True)) == 8 + 12

def test_calc_num_weights3_7():
    assert calc_num_weights3(1, [4], 0, (True, False), (False, True)) == 4 + 4

def test_calc_num_weights3_8():
    assert calc_num_weights3(2, [], 0, (True, False), (False, True)) == 8 + 12
