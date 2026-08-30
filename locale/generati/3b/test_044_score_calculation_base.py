from funzione import score_calculation_base

def test_score_calculation_base_1():
    assert score_calculation_base(0, 0, False, False) == (0, '')

def test_score_calculation_base_2():
    assert score_calculation_base(4, 40, False, False) == (8000, "満貫2000-4000点")

def test_score_calculation_base_3():
    assert score_calculation_base(5, 40, False, False) == (12000, "満貫4000点∀")

def test_score_calculation_base_4():
    assert score_calculation_base(6, 40, True, False) == (18000, "跳满6000点∀")

def test_score_calculation_base_5():
    assert score_calculation_base(8, 40, False, True) == (16000, "倍满4000-8000点")

def test_score_calculation_base_6():
    assert score_calculation_base(11, 40, True, True) == (36000, "三倍满12000点∀")

def test_score_calculation_base_7():
    assert score_calculation_base(12, 40, False, True) == (32000, "役满8000-16000点")
