from funzione import idx_for_diag_se_from_bl

def test_idx_for_diag_se_from_bl_1():
    gen = idx_for_diag_se_from_bl(num_rows=2, num_cols=3)
    result = list(gen)
    assert len(result) == 6
    assert result[0] == (1, 0)
    assert result[-1] == (0, 2)

def test_idx_for_diag_se_from_bl_2():
    gen = idx_for_diag_se_from_bl(num_rows=3, num_cols=4)
    result = list(gen)
    assert len(result) == 10
    assert result[0] == (2, 0)
    assert result[-1] == (0, 3)

def test_idx_for_diag_se_from_bl_3():
    gen = idx_for_diag_se_from_bl(num_rows=4, num_cols=5)
    result = list(gen)
    assert len(result) == 14
    assert result[0] == (3, 0)
    assert result[-1] == (0, 4)

def test_idx_for_diag_se_from_bl_4():
    gen = idx_for_diag_se_from_bl(num_rows=5, num_cols=6)
    result = list(gen)
    assert len(result) == 18
    assert result[0] == (4, 0)
    assert result[-1] == (0, 5)

def test_idx_for_diag_se_from_bl_5():
    gen = idx_for_diag_se_from_bl(num_rows=2, num_cols=2)
    result = list(gen)
    assert len(result) == 3
    assert result[0] == (1, 0)
    assert result[-1] == (0, 1)

def test_idx_for_diag_se_from_bl_6():
    gen = idx_for_diag_se_from_bl(num_rows=2, num_cols=2)
    next(gen)
    result = list(gen)
    assert len(result) == 3
    assert result[0] == (1, 1)
    assert result[-1] == (0, 1)

def test_idx_for_diag_se_from_bl_7():
    gen = idx_for_diag_se_from_bl(num_rows=2, num_cols=2)
    next(gen); next(gen)
    result = list(gen)
    assert len(result) == 3
    assert result[0] == (1, 2)
    assert result[-1] == (0, 2)

def test_idx_for_diag_se_from_bl_8():
    gen = idx_for_diag_se_from_bl(num_rows=2, num_cols=2)
    next(gen); next(gen); next(gen)
    result = list(gen)
    assert len(result) == 3
    assert result[0] == (1, 3)
    assert result[-1] == (0, 3)
