test_calculate_possibility_1.py
def test_calculate_possibility_1():
    assert calculate_possibility(0, 0, 0) == 1
    assert calculate_possibility(0, 0, -1) == 0.4
    assert calculate_possibility(0, 1, 0) == 1
    assert calculate_possibility(0, 1, -1) == 0.4
    assert calculate_possibility(0, 2, 0) == 1
    assert calculate_possibility(0, 2, -1) == 0.4
    assert calculate_possibility(0, 3, 0) == 1
    assert calculate_possibility(0, 3, -1) == 0.4

test_calculate_possibility_2.py
def test_calculate_possibility_2():
    assert calculate_possibility(1, 0, 0) == 0.01
    assert calculate_possibility(1, 0, -1) == 0.4
    assert calculate_possibility(1, 1, 0) == 0.01
    assert calculate_possibility(1, 1, -1) == 0.4
    assert calculate_possibility(1, 2, 0) == 0.01
    assert calculate_possibility(1, 2, -1) == 0.4

test_calculate_possibility_3.py
def test_calculate_possibility_3():
    assert calculate_possibility(2, 0, 0) == 0.01
    assert calculate_possibility(2, 0, -1) == 0.4
    assert calculate_possibility(2, 1, 0) == 0.01
    assert calculate_possibility(2, 1, -1) == 0.4
    assert calculate_possibility(2, 2, 0) == 0.01
    assert calculate_possibility(2, 2, -1) == 0.4

test_calculate_possibility_4.py
def test_calculate_possibility_4():
    assert calculate_possibility(3, 0, 0) == 0.01
    assert calculate_possibility(3, 0, -1) == 0.4
    assert calculate_possibility(3, 1, 0) == 0.01
    assert calculate_possibility(3, 1, -1) == 0.4
    assert calculate_possibility(3, 2, 0) == 0.01
    assert calculate_possibility(3, 2, -1) == 0.4

test_calculate_possibility_5.py
def test_calculate_possibility_5():
    assert calculate_possibility(4, 0, 0) == 0.01
    assert calculate_possibility(4, 0, -1) == 0.4
    assert calculate_possibility(4, 1, 0) == 0.01
    assert calculate_possibility(4, 1, -1) == 0.4
    assert calculate_possibility(4, 2, 0) == 0.01
    assert calculate_possibility(4, 2, -1) == 0.4

test_calculate_possibility_6.py
def test_calculate_possibility_6():
    assert calculate_possibility(5, 0, 0) == 0.01
    assert calculate_possibility(5, 0, -1) == 0.4
    assert calculate_possibility(5, 1, 0) == 0.01
    assert calculate_possibility(5, 1, -1) == 0.4
    assert calculate_possibility(5, 2, 0) == 0.01
    assert calculate_possibility(5, 2, -1) == 0.4

test_calculate_possibility_7.py
def test_calculate_possibility_7():
    assert calculate_possibility(6, 0, 0) == 0.01
    assert calculate_possibility(6, 0, -1) == 0.4
    assert calculate_possibility(6, 1, 0) == 0.01
    assert calculate_possibility(6, 1, -1) == 0.4
    assert calculate_possibility(6,
