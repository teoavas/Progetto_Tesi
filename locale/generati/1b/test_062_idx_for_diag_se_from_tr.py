```python
import pytest

def test_idx_for_diag_se_from_tr_1():
    assert set(idx_for_diag_se_from_tr()) == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)}

def test_idx_for_diag_se_from_tr_2():
    assert set(idx_for_diag_se_from_tr(3)) == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}

def test_idx_for_diag_se_from_tr_3():
    assert set(idx_for_diag_se_from_tr(4)) == {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)}

def test_idx_for_diag_se_from_tr_4():
    assert set(idx_for_diag_se_from_tr(5)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)}

def test_idx_for_diag_se_from_tr_5():
    assert set(idx_for_diag_se_from_tr(6)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)}

def test_idx_for_diag_se_from_tr_6():
    assert set(idx_for_diag_se_from_tr(7)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)}

def test_idx_for_diag_se_from_tr_7():
    assert set(idx_for_diag_se_from_tr(8)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)}

def test_idx_for_diag_se_from_tr_8():
    assert set(idx_for_diag_se_from_tr(9)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)}

def test_idx_for_diag_se_from_tr_9():
    assert set(idx_for_diag_se_from_tr(10)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9)}

def test_idx_for_diag_se_from_tr_10():
    assert set(idx_for_diag_se_from_tr(11)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10)}

def test_idx_for_diag_se_from_tr_11():
    assert set(idx_for_diag_se_from_tr(12)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
