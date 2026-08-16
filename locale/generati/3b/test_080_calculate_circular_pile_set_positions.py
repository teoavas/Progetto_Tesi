from funzione import calculate_circular_pile_set_positions

def test_calculate_circular_pile_set_positions_1():
    assert calculate_circular_pile_set_positions((0, 0), (1, 2), (-1, -1), 0, 3, 1) == (1, 2)

def test_calculate_circular_pile_set_positions_2():
    assert calculate_circular_pile_set_positions((5, 5), (1, 1), (2, 2), 1, 4, -1) == (6, 6)

def test_calculate_circular_pile_set_positions_3():
    assert calculate_circular_pile_set_positions((10, 10), (2, 3), (-1, -1), 0, 5, 1) == (12, 13)

def test_calculate_circular_pile_set_positions_4():
    assert calculate_circular_pile_set_positions((-5, -5), (1, 1), (2, 2), 3, 6, -1) == (-4, -4)

def test_calculate_circular_pile_set_positions_5():
    assert calculate_circular_pile_set_positions((0, 0), (1, 2), (2, 2), 0, 3, 1) == (1, 2)

def test_calculate_circular_pile_set_positions_6():
    with pytest.raises(ValueError):
        calculate_circular_pile_set_positions((0, 0), (1, 2), (-1, -1), 0, 3, None)

def test_calculate_circular_pile_set_positions_7():
    assert calculate_circular_pile_set_positions((10, 10), (2, 3), (-1, -1), 0, 5, 1) == (12, 13)
