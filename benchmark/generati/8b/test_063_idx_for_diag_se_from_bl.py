from funzione import idx_for_diag_se_from_bl

def test_idx_for_diag_se_from_bl_1():
    gen = idx_for_diag_se_from_bl(num_rows=2, num_cols=3)
    assert list(gen) == [(1, 0), (0, 1)]

def test_idx_for_diag_se_from_bl_2():
    gen = idx_for_diag_se_from_bl(num_rows=2, num_cols=3)
    assert list(gen) == [(1, 0), (0, 1)]

def test_idx_for_diag_se_from_bl_3():
    gen = idx_for_diag_se_from_bl(num_rows=3, num_cols=3)
    assert list(gen) == [(2, 0), (1, 1), (0, 2), (2, 1), (1, 0), (0, 1), (2, 2)]

def test_idx_for_diag_se_from_bl_4():
    gen = idx_for_diag_se_from_bl(num_rows=3, num_cols=3)
    assert list(gen) == [(2, 0), (1, 1), (0, 2), (2, 1), (1, 0), (0, 1), (2, 2)]

def test_idx_for_diag_se_from_bl_5():
    gen = idx_for_diag_se_from_bl(num_rows=3, num_cols=2)
    assert list(gen) == [(2, 0), (1, 1), (0, 2)]

def test_idx_for_diag_se_from_bl_6():
    gen = idx_for_diag_se_from_bl(num_rows=3, num_cols=2)
    assert list(gen) == [(2, 0), (1, 1), (0, 2)]

def test_idx_for_diag_se_from_bl_7():
    gen = idx_for_diag_se_from_bl(num_rows=2, num_cols=2)
    assert list(gen) == [(1, 0), (0, 1)]

def test_idx_for_diag_se_from_bl_8():
    gen = idx_for_diag_se_from_bl(num_rows=2, num_cols=2)
    assert list(gen) == [(1, 0), (0, 1)]
