import pytest

def test_coord_finder_1():
    assert coord_finder("FF") == (1, 0)
    assert coord_finder("FL") == (-1, 0)
    assert coord_finder("FR") == (0, -1)

def test_coord_finder_2():
    assert coord_finder("LF") == (-1, 0)
    assert coord_finder("LR") == (0, -1)
    assert coord_finder("RR") == (0, 1)

def test_coord_finder_3():
    assert coord_finder("FFL") == (-1, -1)
    assert coord_finder("FLR") == (-1, 0)
    assert coord_finder("FRL") == (1, 0)

def test_coord_finder_4():
    assert coord_finder("FFF") == (0, 0)
    assert coord_finder("FFL") == (-1, -1)
    assert coord_finder("FLR") == (-1, 0)

def test_coord_finder_5():
    assert coord_finder("RLF") == (0, -1)
    assert coord_finder("RFR") == (1, -1)
    assert coord_finder("RRL") == (1, 0)

def test_coord_finder_6():
    assert coord_finder("FFF") == (0, 0)
    assert coord_finder("FFL") == (-1, -1)
    assert coord_finder("FLR") == (-1, 0)

def test_coord_finder_7():
    assert coord_finder("RLF") == (0, -1)
    assert coord_finder("RFR") == (1, -1)
    assert coord_finder("RRL") == (1, 0)

def test_coord_finder_8():
    assert coord_finder("FFF") == (0, 0)
    assert coord_finder("FFL") == (-1, -1)
    assert coord_finder("FLR") == (-1, 0)
