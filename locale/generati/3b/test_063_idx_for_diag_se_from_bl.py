from funzione import idx_for_diag_se_from_bl

def test_idx_for_diag_se_from_bl_1():
    assert list(idx_for_diag_se_from_bl(2, 3)) == [(0, 0), (0, 1), (0, 2)]

def test_idx_for_diag_se_from_bl_2():
    assert list(idx_for_diag_se_from_bl(3, 4)) == [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3)]

def test_idx_for_diag_se_from_bl_3():
    assert list(idx_for_diag_se_from_bl(4, 5)) == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4)]

def test_idx_for_diag_se_from_bl_4():
    assert list(idx_for_diag_se_from_bl(5, 6)) == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 2), (2, 3), (2, 4), (2, 5)]

def test_idx_for_diag_se_from_bl_5():
    assert list(idx_for_diag_se_from_bl(6, 7)) == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6)]

def test_idx_for_diag_se_from_bl_6():
    assert list(idx_for_diag_se_from_bl(7, 8)) == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)]

def test_idx_for_diag_se_from_bl_7():
    assert list(idx_for_diag_se_from_bl(8, 9)) == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)]
