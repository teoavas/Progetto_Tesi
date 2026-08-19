```python
import pytest

def test_idx_for_diag_se_from_bl_1():
    assert set(idx_for_diag_se_from_bl()) == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)}

def test_idx_for_diag_se_from_bl_2():
    assert set(idx_for_diag_se_from_bl(3)) == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}

def test_idx_for_diag_se_from_bl_3():
    assert set(idx_for_diag_se_from_bl(4)) == {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)}

def test_idx_for_diag_se_from_bl_4():
    assert set(idx_for_diag_se_from_bl(5)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)}

def test_idx_for_diag_se_from_bl_5():
    assert set(idx_for_diag_se_from_bl(6)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)}

def test_idx_for_diag_se_from_bl_6():
    assert set(idx_for_diag_se_from_bl(7)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)}

def test_idx_for_diag_se_from_bl_7():
    assert set(idx_for_diag_se_from_bl(8)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)}

def test_idx_for_diag_se_from_bl_8():
    assert set(idx_for_diag_se_from_bl(9)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)}

def test_idx_for_diag_se_from_bl_9():
    assert set(idx_for_diag_se_from_bl(10)) == {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9)}

def test_idx_for_diag_se_from_bl_10():
    assert set(idx_for_diag_se_from_bl(11)) == {(0, 0), (0, 1),
