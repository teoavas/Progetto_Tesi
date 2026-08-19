from funzione import idx_for_diag_se_from_tr

def test_idx_for_diag_se_from_tr_1():
    gen = idx_for_diag_se_from_tr(num_rows=2, num_cols=3)
    next(gen)  # advance to first element
    assert list(gen) == [(0, 2), (1, 2)]

def test_idx_for_diag_se_from_tr_2():
    gen = idx_for_diag_se_from_tr(num_rows=5, num_cols=3)
    next(gen)  # advance to first element
    assert list(gen)[:10] == [(0, 3), (1, 3), (2, 3), (0, 2), (1, 2),
                              (0, 1), (4, 3), (4, 2), (4, 1)]

def test_idx_for_diag_se_from_tr_3():
    gen = idx_for_diag_se_from_tr(num_rows=5, num_cols=5)
    next(gen)  # advance to first element
    assert list(gen)[:15] == [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5),
                             (0, 4), (1, 4), (2, 4), (3, 4),
                             (0, 3), (1, 3), (2, 3), (0, 2),
                             (4, 5), (4, 4), (4, 3)]

def test_idx_for_diag_se_from_tr_4():
    gen = idx_for_diag_se_from_tr(num_rows=10, num_cols=5)
    next(gen)  # advance to first element
    assert list(gen)[:25] == [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5),
                             (0, 4), (1, 4), (2, 4), (3, 4),
                             (0, 3), (1, 3), (2, 3), (0, 2),
                             (9, 5), (9, 4), (9, 3),
                             (8, 5), (8, 4), (8, 3)]

def test_idx_for_diag_se_from_tr_5():
    gen = idx_for_diag_se_from_tr(num_rows=10, num_cols=2)
    next(gen)  # advance to first element
    assert list(gen)[:15] == [(0, 2), (1, 2),
                             (0, 1)]

def test_idx_for_diag_se_from_tr_6():
    gen = idx_for_diag_se_from_tr(num_rows=10, num_cols=3)
    next(gen)  # advance to first element
    assert list(gen)[:20] == [(0, 3), (1, 3), (2, 3),
                             (0, 2), (1, 2),
                             (0, 1)]

def test_idx_for_diag_se_from_tr_7():
    gen = idx_for_diag_se_from_tr(num_rows=10, num_cols=5)
    next(gen)  # advance to first element
    assert list(gen)[:25] == [(0, 5), (1, 5), (2, 5),
                             (0, 4), (1, 4),
                             (9, 5)]
