from funzione import cal_overlap_neg_strand

def test_cal_overlap_neg_strand_1():
    assert cal_overlap_neg_strand(1, 5, 3, 7) == "Complete overlap"

def test_cal_overlap_neg_strand_2():
    assert cal_overlap_neg_strand(1, 3, 5, 7) == "No overlap"

def test_cal_overlap_neg_strand_3():
    assert cal_overlap_neg_strand(1, 5, 7, 9) == "No overlap"

def test_cal_overlap_neg_strand_4():
    assert cal_overlap_neg_strand(1, 5, 4, 6) == 0.5

def test_cal_overlap_neg_strand_5():
    assert cal_overlap_neg_strand(1, 5, 2, 4) == "Complete overlap"

def test_cal_overlap_neg_strand_6():
    assert cal_overlap_neg_strand(1, 5, 6, 8) == "No overlap"

def test_cal_overlap_neg_strand_7():
    assert cal_overlap_neg_strand(1, 5, 3, 5) == 1.0

def test_cal_overlap_neg_strand_8():
    assert cal_overlap_neg_strand(1, 5, 2, 6) == 0.5
