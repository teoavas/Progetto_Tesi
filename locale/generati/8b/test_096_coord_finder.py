from funzione import coord_finder

def test_coord_finder_1():
    assert coord_finder(["F", "L", "F"]) == (2, 0)

def test_coord_finder_2():
    assert coord_finder(["R", "F", "R", "F"]) == (-1, -1)

def test_coord_finder_3():
    assert coord_finder(["L", "F", "L", "F"]) == (-1, 2)

def test_coord_finder_4():
    assert coord_finder(["F", "F", "F", "F"]) == (4, 0)

def test_coord_finder_5():
    assert coord_finder(["R", "R", "R", "R"]) == (-3, -3)

def test_coord_finder_6():
    assert coord_finder(["L", "L", "L", "L"]) == (1, 2)
