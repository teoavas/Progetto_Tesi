import pytest

def test_initiate_board_1():
    assert initiate_board() == {"(0, 3)": "red", "(2, -3)": "green"}

def test_initiate_board_2():
    assert initiate_board() == {"(-3, 0)": "red", ("-3, 3)": "blue"}

def test_initiate_board_3():
    assert initiate_board() == {"(1, 1)": "black", "(1, -1)": "black"}

def test_initiate_board_4():
    assert initiate_board() == {"(-2, 0)": "red", ("-2, -3)": "green"}

def test_initiate_board_5():
    assert initiate_board() == {"(0, 0)": "black", "(0, -1)": "black"}

def test_initiate_board_6():
    assert initiate_board() == {"(-4, 0)": "red", ("-4, -3)": "green"}

def test_initiate_board_7():
    assert initiate_board() == {"(2, 2)": "blue", "(2, -2)": "blue"}
