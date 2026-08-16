from funzione import next_point_in_8_neigh

def test_next_point_in_8_neigh_1():
    assert next_point_in_8_neigh((0, 0), (0, 0)) == (0, -1)

def test_next_point_in_8_neigh_2():
    assert next_point_in_8_neigh((0, 0), (1, 0)) == (-1, 0)

def test_next_point_in_8_neigh_3():
    assert next_point_in_8_neigh((0, 0), (0, 1)) == (0, -1)

def test_next_point_in_8_neigh_4():
    assert next_point_in_8_neigh((0, 0), (0, 2)) == (-1, 1)

def test_next_point_in_8_neigh_5():
    assert next_point_in_8_neigh((0, 0), (1, 1)) == (-1, 1)

def test_next_point_in_8_neigh_6():
    assert next_point_in_8_neigh((0, 0), (2, 0)) == (-1, -1)

def test_next_point_in_8_neigh_7():
    assert next_point_in_8_neigh((0, 0), (0, 3)) == (-1, -1)

def test_next_point_in_8_neigh_8():
    assert next_point_in_8_neigh((0, 0), (2, 2)) == (-1, -1)
