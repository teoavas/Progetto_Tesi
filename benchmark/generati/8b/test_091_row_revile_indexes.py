from funzione import row_revile_indexes

def test_row_revile_indexes_1():
    lines_vars = [('X', 'value'), ('dX', 'value'), ('Y', 'value'), ('dY', 'value')]
    assert row_revile_indexes(lines_vars) == (0, 1, 2, 3)

def test_row_revile_indexes_2():
    lines_vars = [('X', 'value'), ('dX', 'value'), ('Y', 'value')]
    assert row_revile_indexes(lines_vars) == (-1, -1, -1, -1)

def test_row_revile_indexes_3():
    lines_vars = [('X', 'value'), ('dX', 'value'), ('dY', 'value')]
    assert row_revile_indexes(lines_vars) == (0, 1, -1, -1)

def test_row_revile_indexes_4():
    lines_vars = [('X', 'value'), ('Y', 'value'), ('dX', 'value'), ('dY', 'value')]
    assert row_revile_indexes(lines_vars) == (0, -1, 1, -1)

def test_row_revile_indexes_5():
    lines_vars = [('X', 'value'), ('Y', 'value'), ('dX', 'value'), ('dY', 'value')]
    assert row_revile_indexes(lines_vars, labale_X='x', labale_dX='dx', labale_Y='y', labale_dY='dy') == (0, 1, 2, 3)

def test_row_revile_indexes_6():
    lines_vars = [('X', 'value'), ('dX', 'value'), ('Y', 'value'), ('dY', 'value')]
    assert row_revile_indexes(lines_vars, labale_X='X', labale_dX='dX', labale_Y='Y', labale_dY='dY', index_x=0, index_dx=1, index_y=2, index_dy=3) == (0, 1, 2, 3)

def test_row_revile_indexes_7():
    lines_vars = [('X', 'value'), ('dX', 'value'), ('Y', 'value'), ('dY', 'value')]
    assert row_revile_indexes(lines_vars, labale_X='X', labale_dX='dX', labale_Y='Y', labale_dY='dY', index_x=10, index_dx=20, index_y=30, index_dy=40) == (10, 20, 30, 40)
