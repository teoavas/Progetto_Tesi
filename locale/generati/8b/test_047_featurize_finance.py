from funzione import featurize_finance

def test_featurize_finance_1():
    assert featurize_finance(0, 100000) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_featurize_finance_2():
    assert featurize_finance(50000, 100000) == [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

def test_featurize_finance_3():
    assert featurize_finance(750000, 100000) == [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

def test_featurize_finance_4():
    assert featurize_finance(2500000, 100000) == [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

def test_featurize_finance_5():
    assert featurize_finance(12500000, 100000) == [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

def test_featurize_finance_6():
    assert featurize_finance(62500000, 100000) == [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]

def test_featurize_finance_7():
    assert featurize_finance(125000000, 100000) == [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
