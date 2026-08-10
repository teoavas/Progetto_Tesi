from funzione import is_degree_in_degree_range

def test_is_degree_in_degree_range_1():
    assert is_degree_in_degree_range(0, 90, 45) == True

def test_is_degree_in_degree_range_2():
    assert is_degree_in_degree_range(0, 90, 180) == False

def test_is_degree_in_degree_range_3():
    assert is_degree_in_degree_range(-90, 0, -45) == True

def test_is_degree_in_degree_range_4():
    assert is_degree_in_degree_range(90, 0, 45) == True

def test_is_degree_in_degree_range_5():
    assert is_degree_in_degree_range(0, 0, 0) == True

def test_is_degree_in_degree_range_6():
    assert is_degree_in_degree_range(180, -180, 0) == True

def test_is_degree_in_degree_range_7():
    assert is_degree_in_degree_range(-180, 180, -90) == True
