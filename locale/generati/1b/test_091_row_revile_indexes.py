import pytest

def test_row_revile_indexes_1():
    assert row_revile_indexes(['a', 'b'], labale_X='X') == (0, -1, -1, -1)

def test_row_revile_indexes_2():
    assert row_revile_indexes(['A', 'B']) == (-1, -1, -1, -1)

def test_row_revile_indexes_3():
    assert row_revile_indexes(['a', 'b'], labale_X='X', labale_dX=0) == (0, 0, -1, -1)

def test_row_revile_indexes_4():
    assert row_revile_indexes(['A', 'B']) == (-1, -1, -1, -1)

def test_row_revile_indexes_5():
    assert row_revile_indexes(['a', 'b'], labale_X='X', labale_dY=0) == (0, 0, -1, -1)

def test_row_revile_indexes_6():
    assert row_revile_indexes(['A', 'B']) == (-1, -1, -1, -1)

def test_row_revile_indexes_7():
    assert row_revile_indexes(['a', 'b'], labale_X='X', labale_dY=0) == (0, 0, -1, -1)
