from funzione import initiate_board

def test_initiate_board_1():
    result = initiate_board()
    assert len(result) == 13
    assert (0, -3) in result
    assert (-3, 0) in result
    assert (2, 1) in result

def test_initiate_board_2():
    result = initiate_board()
    assert "red" in result.values()
    assert "green" in result.values()
    assert "blue" in result.values()

def test_initiate_board_3():
    result = initiate_board()
    assert (0, 0) not in result

def test_initiate_board_4():
    result = initiate_board()
    assert (-2, -1) in result
    assert (-1, -2) in result

def test_initiate_board_5():
    result = initiate_board()
    assert "red" == result.get((-3, 0), None)
    assert "green" == result.get((0, -3), None)

def test_initiate_board_6():
    result = initiate_board()
    assert (2, 1) in result
    assert "blue" == result[(2, 1)]

def test_initiate_board_7():
    result = initiate_board()
    assert len(result.keys()) == 13

def test_initiate_board_8():
    result = initiate_board()
    assert (-3, -3) not in result
