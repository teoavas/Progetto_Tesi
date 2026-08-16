from funzione import featurize_finance

def test_featurize_finance_1():
    assert featurize_finance(0, 10000) == [1]

def test_featurize_finance_2():
    assert featurize_finance(50000, 10000) == [1, 1]

def test_featurize_finance_3():
    assert featurize_finance(100000, 10000) == [1, 1, 1]

def test_featurize_finance_4():
    assert featurize_finance(500000, 10000) == [1, 1, 1, 1]

def test_featurize_finance_5():
    assert featurize_finance(1000000, 10000) == [1, 1, 1, 1, 1]

def test_featurize_finance_6():
    assert featurize_finance(5000000, 10000) == [1, 1, 1, 1, 1, 1]

def test_featurize_finance_7():
    assert featurize_finance(10000000, 10000) == [1, 1, 1, 1, 1, 1, 1]
