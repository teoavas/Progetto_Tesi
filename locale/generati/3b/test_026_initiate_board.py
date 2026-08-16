from funzione import initiate_board

def test_initiate_board_1():
    assert initiate_board() != {}

def test_initiate_board_2():
    assert len(initiate_board()) > 0

def test_initiate_board_3():
    assert "red" in initiate_board()

def test_initiate_board_4():
    assert "green" in initiate_board()

def test_initiate_board_5():
    assert "blue" in initiate_board()

def test_initiate_board_6():
    board = initiate_board()
    for key, value in board.items():
        assert isinstance(key, tuple)
        assert len(key) == 2
        assert -3 <= key[0] <= 3
        assert -3 <= key[1] <= 3

def test_initiate_board_7():
    board = initiate_board()
    for key, value in board.items():
        if value == "red":
            assert key[0] == -3
        elif value == "green":
            assert key[1] == -3
        elif value == "blue":
            assert key[0] + key[1] == 3
