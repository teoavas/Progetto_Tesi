from funzione import cal_overlap_neg_strand

def test_cal_overlap_neg_strand_1():
    assert cal_overlap_neg_strand(0, 10, 5, 15) == COMP_OVL

def test_cal_overlap_neg_strand_2():
    assert cal_overlap_neg_strand(0, 10, 20, 30) == NO_OVL

def test_cal_overlap_neg_strand_3():
    assert round(cal_overlap_neg_strand(1, 5, 4, 8), 2) == 0.50

def test_cal_overlap_neg_strand_4():
    assert cal_overlap_neg_strand(10, 20, 15, 25) == COMP_OVL

def test_cal_overlap_neg_strand_5():
    assert round(cal_overlap_neg_strand(1, 3, 2, 6), 2) == 0.33

def test_cal_overlap_neg_strand_6():
    assert cal_overlap_neg_strand(15, 25, 20, 30) == NO_OVL

def test_cal_overlap_neg_strand_7():
    assert round(cal_overlap_neg_strand(5, 10, 8, 12), 2) == 0.40
