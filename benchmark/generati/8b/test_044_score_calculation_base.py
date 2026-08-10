from funzione import score_calculation_base

def test_score_calculation_base_1():
    assert score_calculation_base(0, 0, False, False) == (0, '')

def test_score_calculation_base_2():
    assert score_calculation_base(4, 40, False, False) == (8000, "満貫2000-4000点")

def test_score_calculation_base_3():
    assert score_calculation_base(4, 70, False, False) == (8000, "満貫2000-4000点")

def test_score_calculation_base_4():
    assert score_calculation_base(4, 40, True, False) == (12000, "満貫12000点")

def test_score_calculation_base_5():
    assert score_calculation_base(4, 40, False, True) == (8000, "満貫2000-4000点∀")

def test_score_calculation_base_6():
    assert score_calculation_base(5, 0, False, False) == (8000, "満貫2000-4000点")

def test_score_calculation_base_7():
    assert score_calculation_base(6, 0, False, False) == (12000, "跳満3000-6000点")

def test_score_calculation_base_8():
    assert score_calculation_base(11, 0, False, False) == (24000, "三倍満6000-12000点")
