from funzione import get_next_queen_recursion_coordinates

def test_get_next_queen_recursion_coordinates_1():
    assert get_next_queen_recursion_coordinates(Square(0, 0), 0, Square(1, 1), 1) == (2, 2)

def test_get_next_queen_recursion_coordinates_2():
    assert get_next_queen_recursion_coordinates(Square(3, 4), -5, Square(6, 8), -7) == (-9, -10)

def test_get_next_queen_recursion_coordinates_3():
    assert get_next_queen_recursion_coordinates(Square(0, 0), 1, Square(1, 1), 2) == (2, 2)

def test_get_next_queen_recursion_coordinates_4():
    assert get_next_queen_recursion_coordinates(Square(5, 6), -3, Square(7, 8), -5) == (-5, -6)

def test_get_next_queen_recursion_coordinates_5():
    assert get_next_queen_recursion_coordinates(Square(0, 0), 2, Square(1, 1), 4) == (4, 4)

def test_get_next_queen_recursion_coordinates_6():
    assert get_next_queen_recursion_coordinates(Square(3, 4), -5, Square(6, 8), -7) == (-9, -10)

def test_get_next_queen_recursion_coordinates_7():
    assert get_next_queen_recursion_coordinates(Square(0, 0), 1, Square(1, 1), 2) == (2, 2)

def test_get_next_queen_recursion_coordinates_8():
    assert get_next_queen_recursion_coordinates(Square(5, 6), -3, Square(7, 8), -5) == (-5, -6)
