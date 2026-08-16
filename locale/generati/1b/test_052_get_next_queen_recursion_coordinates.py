import pytest

class Square:
    def __init__(self, rank, file):
        self.rank = rank
        self.file = file

def get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square, vertical_coordinate):
    next_square_rank = current_square.rank
    next_square_file = current_square.file
    if vertical_coordinate == horizontal_coordinate:
        if vertical_coordinate > 0:
            next_square_rank = target_square.rank + 1
            next_square_file = target_square.file + 1
        elif vertical_coordinate < 0:
            next_square_rank = target_square.rank - 1
            next_square_file = target_square.file - 1
    elif vertical_coordinate == -horizontal_coordinate:
        if vertical_coordinate > 0:
            next_square_rank = target_square.rank + 1
            next_square_file = target_square.file - 1
        elif vertical_coordinate < 0:
            next_square_rank = target_square.rank - 1
            next_square_file = target_square.file + 1
    elif horizontal_coordinate == 0:
        if vertical_coordinate > 0:
            next_square_rank = target_square.rank + 1
        elif vertical_coordinate < 0:
            next_square_rank = target_square.rank - 1
    elif vertical_coordinate == 0:
        if horizontal_coordinate > 0:
            next_square_file = target_square.file + 1
        elif horizontal_coordinate < 0:
            next_square_file = target_square.file - 1
    return next_square_file, next_square_rank

def test_get_next_queen_recursion_coordinates_1():
    current_square = Square(2, 4)
    horizontal_coordinate = 3
    vertical_coordinate = 5
    expected_result = (6, 7)
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square=Square(2, 4), vertical_coordinate=vertical_coordinate) == expected_result

def test_get_next_queen_recursion_coordinates_2():
    current_square = Square(1, 3)
    horizontal_coordinate = 0
    vertical_coordinate = -1
    expected_result = (2, 1)
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square=Square(1, 3), vertical_coordinate=vertical_coordinate) == expected_result

def test_get_next_queen_recursion_coordinates_3():
    current_square = Square(5, 7)
    horizontal_coordinate = -2
    vertical_coordinate = 0
    expected_result = (6, 8)
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square=Square(5, 7), vertical_coordinate=vertical_coordinate) == expected_result

def test_get_next_queen_recursion_coordinates_4():
    current_square = Square(3, 1)
    horizontal_coordinate = 0
    vertical_coordinate = -2
    expected_result = (4, 3)
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square=Square(3, 1), vertical_coordinate=vertical_coordinate) == expected_result

def test_get_next_queen_recursion_coordinates_5():
    current_square = Square(2, 6)
    horizontal_coordinate = -1
    vertical_coordinate = 0
    expected_result = (3, 2)
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square=Square(2, 6), vertical_coordinate=vertical_coordinate) == expected_result

def test_get_next_queen_recursion_coordinates_6():
    current_square = Square(4, 8)
    horizontal_coordinate = -1
    vertical_coordinate = -1
    expected_result = (5, 4)
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square=Square(4, 8), vertical_coordinate=vertical_coordinate) == expected_result

def test_get_next_queen_recursion_coordinates_7():
    current_square = Square(1, 2)
    horizontal_coordinate = -1
    vertical_coordinate = 0
    expected_result = (2, 1)
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square=Square(1, 2), vertical_coordinate=vertical_coordinate) == expected_result

def test_get_next_queen_recursion_coordinates_8():
    current_square = Square(5, 7)
    horizontal_coordinate = -1
    vertical_coordinate = -1
    expected_result = (6, 6)
    assert get_next_queen_recursion_coordinates(current_square, horizontal_coordinate, target_square=Square(5, 7), vertical_coordinate=vertical_coordinate) == expected_result
