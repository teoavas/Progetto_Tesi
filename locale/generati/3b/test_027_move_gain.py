from funzione import move_gain

def test_move_gain_1():
    assert move_gain((0, 0), 0, 0, 0, {((0, 0)): [1, 2]}, {(0, 0): 0}, 0) == 3

def test_move_gain_2():
    assert move_gain((0, 1), 0, 0, 1, {((0, 1)): [1, 2]}, {(0, 1): 0}, 0) == 1

def test_move_gain_3():
    assert move_gain((0, 0), 0, 1, 0, {((0, 0)): [1, 2]}, {(0, 0): 0}, 0) == 1

def test_move_gain_4():
    assert move_gain((0, 0), 0, 0, 0, {((0, 0)): [1, 2]}, {(0, 0): 0}, 1) == 3

def test_move_gain_5():
    assert move_gain((0, 0), 0, 0, 0, {((0, 0)): [1, 2]}, {(0, 0): 0}, 10) == 13

def test_move_gain_6():
    assert move_gain((0, 0), 0, 0, 0, {((0, 0)): [1, 2]}, {(0, 0): 0}, 100) == 113

def test_move_gain_7():
    assert move_gain((0, 0), 0, 0, 0, {((0, 0)): [1, 2]}, {(0, 0): 0}, 1000) == 1166
