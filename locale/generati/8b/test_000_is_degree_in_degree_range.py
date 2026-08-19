from funzione import is_degree_in_degree_range

def test_is_degree_in_degree_range_1():
    assert is_degree_in_degree_range(0, 180, 90) == True

def test_is_degree_in_degree_range_2():
    assert is_degree_in_degree_range(-45, -135, -120) == False

def test_is_degree_in_degree_range_3():
    assert is_degree_in_degree_range(200, 300, 250) == True

def test_is_degree_in_degree_range_4():
    assert is_degree_in_degree_range(-180, 0, -90) == True

def test_is_degree_in_degree_range_5():
    assert is_degree_in_degree_range(45, 135, 120) == False

def test_is_degree_in_degree_range_6():
    assert is_degree_in_degree_range(270, 360, 300) == True
