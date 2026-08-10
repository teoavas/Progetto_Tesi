from funzione import move_gain

def test_move_gain_1():
    match = [1, 2, 3]
    i = 1
    m = 2
    nm = 3
    weight_dict = {(1, 2): {(-1,): 0, (0, 0): 1}}
    match_num_dict = {(1, 2, 3): 0}
    match_num = 0
    assert move_gain(match, i, m, nm, weight_dict, match_num_dict, match_num) == 1

def test_move_gain_2():
    match = [1, 2, 3]
    i = 1
    m = 2
    nm = 3
    weight_dict = {(1, 2): {(-1,): 0, (0, 0): 1}}
    match_num_dict = {(1, 2, 3): 0}
    match_num = 0
    assert move_gain(match, i, m, nm, weight_dict, match_num_dict, match_num) == 1

def test_move_gain_3():
    match = [1, 2, 3]
    i = 1
    m = 2
    nm = 3
    weight_dict = {(1, 2): {(-1,): 0, (0, 0): 1}}
    match_num_dict = {(1, 2, 3): 0}
    match_num = 0
    assert move_gain(match, i, m, nm, weight_dict, match_num_dict, match_num) == 1

def test_move_gain_4():
    match = [1, 2, 3]
    i = 1
    m = 2
    nm = 3
    weight_dict = {(1, 2): {(-1,): 0, (0, 0): 1}}
    match_num_dict = {(1, 2, 3): 0}
    match_num = 0
    assert move_gain(match, i, m, nm, weight_dict, match_num_dict, match_num) == 1

def test_move_gain_5():
    match = [1, 2, 3]
    i = 1
    m = 2
    nm = 3
    weight_dict = {(1, 2): {(-1,): 0, (0, 0): 1}}
    match_num_dict = {(1, 2, 3): 0}
    match_num = 0
    assert move_gain(match, i, m, nm, weight_dict, match_num_dict, match_num) == 1

def test_move_gain_6():
    match = [1, 2, 3]
    i = 1
    m = 2
    nm = 3
    weight_dict = {(1, 2): {(-1,): 0, (0, 0): 1}}
    match_num_dict = {(1, 2, 3): 0}
    match_num = 0
    assert move_gain(match, i, m, nm, weight_dict, match_num_dict, match_num) == 1

def test_move_gain_7():
    match = [1, 2, 3]
    i = 1
    m = 2
    nm = 3
    weight_dict = {(1, 2): {(-1,): 0, (0, 0): 1}}
    match_num_dict = {(1, 2, 3): 0}
    match_num = 0
    assert move_gain(match, i, m, nm, weight_dict, match_num_dict, match_num) == 1

def test_move_gain_8():
    match = [1, 2, 3]
    i = 1
    m = 2
    nm = 3
    weight_dict = {(1, 2): {(-1,): 0, (0, 0): 1}}
    match_num_dict = {(1, 2, 3): 0}
    match_num = 0
    assert move_gain(match, i, m, nm, weight_dict, match_num_dict, match_num) == 1
