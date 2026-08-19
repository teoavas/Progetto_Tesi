from funzione import row_revile_indexes

def test_row_revile_indexes_1():
    assert row_revile_indexes([("line1", "X"), ("line2", "dX")]) == (-1, -1, -1, -1)

def test_row_revile_indexes_2():
    assert row_revile_indexes([("line1", "Y"), ("line2", "dY")]) == (-1, -1, -1, -1)

def test_row_revile_indexes_3():
    assert row_revile_indexes([("line1", "X"), ("line2", "Y")]) == (-1, -1, -1, -1)

def test_row_revile_indexes_4():
    assert row_revile_indexes([("line1", "dX"), ("line2", "dY")]) == (-1, -1, -1, -1)

def test_row_revile_indexes_5():
    assert row_revile_indexes([("line1", "X"), ("line2", "dX"), ("line3", "Y")]) == (0, 1, 2, -1)

def test_row_revile_indexes_6():
    assert row_revile_indexes([("line1", "X"), ("line2", "dX"), ("line3", "Y"), ("line4", "dY")]) == (0, 1, 2, 3)

def test_row_revile_indexes_7():
    assert row_revile_indexes([("line1", "X"), ("line2", "dX"), ("line3", "Y"), ("line4", "dY"), ("line5", "Z")]) == (-1, -1, -1, -1)
