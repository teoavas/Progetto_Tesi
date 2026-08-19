import pytest

@pytest.mark.parametrize("s1, e1, s2, e2", [
    (0, 10, -5, 15), (20, 30, -3, 25),
])
def test_cal_overlap_neg_strand_1(s1, e1, s2, e2):
    assert cal_overlap_neg_strand(s1, e1, s2, e2) == COMP_OVL

@pytest.mark.parametrize("s1, e1, s2, e2", [
    (0, 10, -5, 15), (-20, 30, -3, 25),
])
def test_cal_overlap_neg_strand_2(s1, e1, s2, e2):
    assert cal_overlap_neg_strand(s1, e1, s2, e2) == NO_OVL

@pytest.mark.parametrize("s1, e1, s2, e2", [
    (0, 10, -5, 15), (-20, 30, -3, 25),
])
def test_cal_overlap_neg_strand_3(s1, e1, s2, e2):
    assert cal_overlap_neg_strand(s1, e1, s2, e2) == COMP_OVL

@pytest.mark.parametrize("s1, e1, s2, e2", [
    (0, 10, -5, 15), (-20, 30, -3, 25),
])
def test_cal_overlap_neg_strand_4(s1, e1, s2, e2):
    assert cal_overlap_neg_strand(s1, e1, s2, e2) == NO_OVL

@pytest.mark.parametrize("s1, e1, s2, e2", [
    (0, 10, -5, 15), (-20, 30, -3, 25),
])
def test_cal_overlap_neg_strand_5(s1, e1, s2, e2):
    assert cal_overlap_neg_strand(s1, e1, s2, e2) == COMP_OVL

@pytest.mark.parametrize("s1, e1, s2, e2", [
    (0, 10, -5, 15), (-20, 30, -3, 25),
])
def test_cal_overlap_neg_strand_6(s1, e1, s2, e2):
    assert cal_overlap_neg_strand(s1, e1, s2, e2) == NO_OVL

@pytest.mark.parametrize("s1, e1, s2, e2", [
    (0, 10, -5, 15), (-20, 30, -3, 25),
])
def test_cal_overlap_neg_strand_7(s1, e1, s2, e2):
    assert cal_overlap_neg_strand(s1, e1, s2, e2) == COMP_OVL

@pytest.mark.parametrize("s1, e1, s2, e2", [
    (0, 10, -5, 15), (-20, 30, -3, 25),
])
def test_cal_overlap_neg_strand_8(s1, e1, s2, e2):
    assert cal_overlap_neg_strand(s1, e1, s2, e2) == NO_OVL
