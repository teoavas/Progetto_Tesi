from funzione import calculate_possibility

def test_calculate_possibility_1():
    assert calculate_possibility((0, 0, 0), (0, 0, 0), 0) == 1

def test_calculate_possibility_2():
    assert calculate_possibility((0, 0, 0), (0, 0, 0), 90) == 0.4

def test_calculate_possibility_3():
    assert calculate_possibility((0, 0, 0), (1, 1, 1), 0) == 0.01

def test_calculate_possibility_4():
    assert calculate_possibility((1, 1, 1), (0, 0, 0), 90) == 0.4

def test_calculate_possibility_5():
    assert calculate_possibility((2, 2, 2), (3, 3, 3), 0) == 1

def test_calculate_possibility_6():
    assert calculate_possibility((2, 2, 2), (4, 4, 4), 90) == 0.01

def test_calculate_possibility_7():
    assert calculate_possibility((3, 3, 3), (1, 1, 1), 180) == 0.4
