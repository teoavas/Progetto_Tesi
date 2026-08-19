from funzione import get_next_queen_recursion_coordinates

def test_get_next_queen_recursion_coordinates_1():
    current_square = Square(0, 0)
    target_square = Square(2, 3)
    horizontal_coordinate = 1
    vertical_coordinate = 1
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square, vertical_coordinate) == (4, 3)

def test_get_next_queen_recursion_coordinates_2():
    current_square = Square(0, 0)
    target_square = Square(2, 3)
    horizontal_coordinate = -1
    vertical_coordinate = 1
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square, vertical_coordinate) == (4, 1)

def test_get_next_queen_recursion_coordinates_3():
    current_square = Square(0, 0)
    target_square = Square(2, 3)
    horizontal_coordinate = 1
    vertical_coordinate = -1
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square, vertical_coordinate) == (3, 1)

def test_get_next_queen_recursion_coordinates_4():
    current_square = Square(0, 0)
    target_square = Square(2, 3)
    horizontal_coordinate = -1
    vertical_coordinate = -1
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square, vertical_coordinate) == (3, 1)

def test_get_next_queen_recursion_coordinates_5():
    current_square = Square(0, 0)
    target_square = Square(2, 3)
    horizontal_coordinate = 0
    vertical_coordinate = 1
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square, vertical_coordinate) == (4, 3)

def test_get_next_queen_recursion_coordinates_6():
    current_square = Square(0, 0)
    target_square = Square(2, 3)
    horizontal_coordinate = 1
    vertical_coordinate = 0
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square, vertical_coordinate) == (4, 3)

def test_get_next_queen_recursion_coordinates_7():
    current_square = Square(2, 2)
    target_square = Square(1, 1)
    horizontal_coordinate = -1
    vertical_coordinate = 0
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square, vertical_coordinate) == (0, 1)

def test_get_next_queen_recursion_coordinates_8():
    current_square = Square(2, 2)
    target_square = Square(1, 1)
    horizontal_coordinate = 0
    vertical_coordinate = -1
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square, vertical_coordinate) == (1, 0)
