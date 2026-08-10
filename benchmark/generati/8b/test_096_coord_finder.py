from funzione import coord_finder

def test_coord_finder_1():
    assert coord_finder(["F", "F"]) == (2, 0)

def test_coord_finder_2():
    assert coord_finder(["L", "F", "R", "F"]) == (1, 2)

def test_coord_finder_3():
    assert coord_finder(["R", "F", "L", "F"]) == (0, 2)

def test_coord_finder_4():
    assert coord_finder(["F", "L", "F", "L", "F", "L"]) == (0, 4)

def test_coord_finder_5():
    assert coord_finder(["F", "F", "F", "F", "F", "F"]) == (5, 0)

def test_coord_finder_6():
    assert coord_finder(["L", "L", "L", "L", "L", "L"]) == (0, -5)

def test_coord_finder_7():
    assert coord_finder(["R", "R", "R", "R", "R", "R"]) == (0, 5)

def test_coord_finder_8():
    assert coord_finder(["F", "F", "L", "F", "L", "F"]) == (1, 2)
