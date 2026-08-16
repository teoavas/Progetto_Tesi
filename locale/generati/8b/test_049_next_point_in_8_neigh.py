from funzione import next_point_in_8_neigh

def test_next_point_in_8_neigh_1():
    b = (0, 0)
    c = (1, 2)
    assert next_point_in_8_neigh(b, c) == (-1, -1)

def test_next_point_in_8_neigh_2():
    b = (0, 0)
    c = (0, 3)
    assert next_point_in_8_neigh(b, c) == (-1, -1)

def test_next_point_in_8_neigh_3():
    b = (0, 0)
    c = (2, 3)
    assert next_point_in_8_neigh(b, c) == (-1, 0)

def test_next_point_in_8_neigh_4():
    b = (0, 0)
    c = (2, 0)
    assert next_point_in_8_neigh(b, c) == (-1, 1)

def test_next_point_in_8_neigh_5():
    b = (0, 0)
    c = (2, -1)
    assert next_point_in_8_neigh(b, c) == (0, 1)

def test_next_point_in_8_neigh_6():
    b = (0, 0)
    c = (0, -1)
    assert next_point_in_8_neigh(b, c) == (1, 1)

def test_next_point_in_8_neigh_7():
    b = (0, 0)
    c = (-1, -1)
    assert next_point_in_8_neigh(b, c) == (1, 0)
