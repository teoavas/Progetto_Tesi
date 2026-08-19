from funzione import coord_finder

def test_coord_finder_1():
    assert coord_finder("FF") == (1, 0)

def test_coord_finder_2():
    assert coord_finder("LFFR") == (-1, -1)

def test_coord_finder_3():
    assert coord_finder("FLLRF") == (0, -1)

def test_coord_finder_4():
    assert coord_finder("RR") == (0, 0)

def test_coord_finder_5():
    assert coord_finder("LFFLR") == (-2, -1)

def test_coord_finder_6():
    assert coord_finder("FLLRFLLR") == (-1, -1)

def test_coord_finder_7():
    assert coord_finder("FFFF") == (0, 0)
