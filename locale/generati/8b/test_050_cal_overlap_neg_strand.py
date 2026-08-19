from funzione import cal_overlap_neg_strand

def test_cal_overlap_neg_strand_1():
    assert cal_overlap_neg_strand(10, 20, 15, 25) == "Complete overlap"

def test_cal_overlap_neg_strand_2():
    assert cal_overlap_neg_strand(5, 15, 20, 30) == "No overlap"

def test_cal_overlap_neg_strand_3():
    assert cal_overlap_neg_strand(10, 20, 25, 35) == 0.6

def test_cal_overlap_neg_strand_4():
    assert cal_overlap_neg_strand(5, 15, 30, 40) == "No overlap"

def test_cal_overlap_neg_strand_5():
    assert cal_overlap_neg_strand(10, 20, 35, 45) == 0.2

def test_cal_overlap_neg_strand_6():
    assert cal_overlap_neg_strand(15, 25, 10, 20) == "Complete overlap"

def test_cal_overlap_neg_strand_7():
    assert cal_overlap_neg_strand(30, 40, 5, 15) == "No overlap"
