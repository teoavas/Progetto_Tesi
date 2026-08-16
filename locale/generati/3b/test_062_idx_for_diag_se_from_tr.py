from funzione import idx_for_diag_se_from_tr

def test_idx_for_diag_se_from_tr_1():
    assert list(idx_for_diag_se_from_tr(2, 3)) == [(0, 2), (1, 2)]

def test_idx_for_diag_se_from_tr_2():
    assert list(idx_for_diag_se_from_tr(3, 4)) == [(0, 3), (1, 3), (2, 3)]

def test_idx_for_diag_se_from_tr_3():
    assert list(idx_for_diag_se_from_tr(4, 5)) == [(0, 4), (1, 4), (2, 4), (3, 4)]

def test_idx_for_diag_se_from_tr_4():
    assert list(idx_for_diag_se_from_tr(5, 6)) == [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5)]

def test_idx_for_diag_se_from_tr_5():
    assert list(idx_for_diag_se_from_tr(2, 2)) == []

def test_idx_for_diag_se_from_tr_6():
    assert list(idx_for_diag_se_from_tr(1, 3)) == [(0, 2), (1, 2)]

def test_idx_for_diag_se_from_tr_7():
    assert list(idx_for_diag_se_from_tr(3, 1)) == []
