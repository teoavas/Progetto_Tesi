from funzione import calculate_possibility

def test_calculate_possibility_1():
    assert calculate_possibility([0, 0, 10, 10], [0, 0, 10, 10], 0) == 1

def test_calculate_possibility_2():
    assert calculate_possibility([0, 0, 10, 10], [0, 0, 10, 10], 1) == 1

def test_calculate_possibility_3():
    assert calculate_possibility([0, 0, 10, 10], [0, 0, 10, 10], -1) == 1

def test_calculate_possibility_4():
    assert calculate_possibility([0, 0, 10, 10], [0, 0, 9, 9], 1) == 0.4

def test_calculate_possibility_5():
    assert calculate_possibility([0, 0, 10, 10], [0, 0, 9, 9], -1) == 0.4

def test_calculate_possibility_6():
    assert calculate_possibility([0, 0, 10, 10], [0, 0, 9, 9], 0) == 0.4

def test_calculate_possibility_7():
    assert calculate_possibility([0, 0, 10, 10], [0, 0, 8, 8], 1) == 0.01

def test_calculate_possibility_8():
    assert calculate_possibility([0, 0, 10, 10], [0, 0, 8, 8], -1) == 0.01
