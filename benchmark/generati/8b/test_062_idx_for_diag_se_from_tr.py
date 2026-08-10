from funzione import idx_for_diag_se_from_tr

def test_idx_for_diag_se_from_tr_1():
    gen = idx_for_diag_se_from_tr(num_rows=2, num_cols=3)
    assert next(gen) == (0, 2)
    assert next(gen) == (1, 2)
    assert next(gen) == (0, 1)
    assert next(gen) == (1, 1)

def test_idx_for_diag_se_from_tr_2():
    gen = idx_for_diag_se_from_tr(num_rows=2, num_cols=2)
    assert next(gen) == (0, 1)
    assert next(gen) == (1, 1)

def test_idx_for_diag_se_from_tr_3():
    gen = idx_for_diag_se_from_tr(num_rows=3, num_cols=3)
    assert next(gen) == (0, 2)
    assert next(gen) == (1, 2)
    assert next(gen) == (2, 2)
    assert next(gen) == (0, 1)
    assert next(gen) == (1, 1)
    assert next(gen) == (2, 1)
    assert next(gen) == (0, 0)
    assert next(gen) == (1, 0)
    assert next(gen) == (2, 0)

def test_idx_for_diag_se_from_tr_4():
    gen = idx_for_diag_se_from_tr(num_rows=3, num_cols=2)
    assert next(gen) == (0, 1)
    assert next(gen) == (1, 1)
    assert next(gen) == (2, 1)
    assert next(gen) == (0, 0)
    assert next(gen) == (1, 0)
    assert next(gen) == (2, 0)

def test_idx_for_diag_se_from_tr_5():
    gen = idx_for_diag_se_from_tr(num_rows=2, num_cols=1)
    assert next(gen) == (0, 0)
    assert next(gen) == (1, 0)

def test_idx_for_diag_se_from_tr_6():
    gen = idx_for_diag_se_from_tr(num_rows=1, num_cols=2)
    assert next(gen) == (0, 1)
    assert next(gen) == (0, 0)

def test_idx_for_diag_se_from_tr_7():
    gen = idx_for_diag_se_from_tr(num_rows=1, num_cols=1)
    assert next(gen) == (0, 0)
