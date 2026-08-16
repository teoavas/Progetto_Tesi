from funzione import row_revile_indexes

def test_row_revile_indexes_1():
    lines_vars = [('X', 'value'), ('dX', 'value')]
    assert row_revile_indexes(lines_vars) == (-1, -1, -1, -1)

def test_row_revile_indexes_2():
    lines_vars = [('X', 'value'), ('Y', 'value')]
    assert row_revile_indexes(lines_vars) == (0, -1, 1, -1)

def test_row_revile_indexes_3():
    lines_vars = [('X', 'value'), ('dX', 'value'), ('Y', 'value')]
    assert row_revile_indexes(lines_vars) == (0, 1, 2, -1)

def test_row_revile_indexes_4():
    lines_vars = [('X', 'value'), ('dX', 'value'), ('Y', 'value'), ('dY', 'value')]
    assert row_revile_indexes(lines_vars) == (0, 1, 2, 3)

def test_row_revile_indexes_5():
    lines_vars = [('X', 'value'), ('dX', 'value'), ('Y', 'value'), ('dY', 'value'), ('Z', 'value')]
    assert row_revile_indexes(lines_vars) == (0, 1, 2, 3)

def test_row_revile_indexes_6():
    lines_vars = [('X', 'value'), ('dX', 'value'), ('Y', 'value'), ('dY', 'value'), ('Z', 'value')]
    assert row_revile_indexes(lines_vars, labale_X='A') == (0, 1, 2, 3)

def test_row_revile_indexes_7():
    lines_vars = [('X', 'value'), ('dX', 'value'), ('Y', 'value'), ('dY', 'value')]
    assert row_revile_indexes(lines_vars) == (0, 1, 2, -1)
