from funzione import initiate_board

def test_initiate_board_1():
    assert initiate_board() == {(0, -3): 'green', (-3, 0): 'red', (0, 0): 'blue'}

def test_initiate_board_2():
    assert initiate_board[(0, -3)] == 'green'

def test_initiate_board_3():
    assert initiate_board[(-3, 0)] == 'red'

def test_initiate_board_4():
    assert initiate_board[(0, 0)] == 'blue'

def test_initiate_board_5():
    assert initiate_board[(-2, -1)] not in initiate_board.values()

def test_initiate_board_6():
    assert initiate_board[(-3, -3)] not in initiate_board.values()

def test_initiate_board_7():
    assert initiate_board[(-1, -2)] not in initiate_board.values()
