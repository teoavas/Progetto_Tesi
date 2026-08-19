from funzione import calculate_possibility

def test_calculate_possibility_1():
    ind1 = [0, 10, 20]
    ind2 = [0, 15, 25]
    angle1 = 45
    assert calculate_possibility(ind1, ind2, angle1) == 1

def test_calculate_possibility_2():
    ind1 = [0, 10, 20]
    ind2 = [0, 5, 25]
    angle1 = -30
    assert calculate_possibility(ind1, ind2, angle1) == 0.4

def test_calculate_possibility_3():
    ind1 = [1, 10, 20]
    ind2 = [1, 15, 25]
    angle1 = 45
    assert calculate_possibility(ind1, ind2, angle1) == 1

def test_calculate_possibility_4():
    ind1 = [1, 10, 20]
    ind2 = [1, 5, 25]
    angle1 = -30
    assert calculate_possibility(ind1, ind2, angle1) == 0.4

def test_calculate_possibility_5():
    ind1 = [2, 10, 20]
    ind2 = [2, 15, 25]
    angle1 = 45
    assert calculate_possibility(ind1, ind2, angle1) == 1

def test_calculate_possibility_6():
    ind1 = [3, 10, 20]
    ind2 = [3, 5, 25]
    angle1 = -30
    assert calculate_possibility(ind1, ind2, angle1) == 0.4

def test_calculate_possibility_7():
    ind1 = [0, 10, 20]
    ind2 = [0, 15, 5]
    angle1 = 45
    assert calculate_possibility(ind1, ind2, angle1) == 0.01

def test_calculate_possibility_8():
    ind1 = [3, 10, 20]
    ind2 = [3, 15, 25]
    angle1 = -30
    assert calculate_possibility(ind1, ind2, angle1) == 1
