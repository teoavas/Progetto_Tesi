from funzione import featurize_finance

def test_featurize_finance_1():
    assert featurize_finance(0, 100000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

def test_featurize_finance_2():
    assert featurize_finance(100000, 100000) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_featurize_finance_3():
    assert featurize_finance(500000, 100000) == [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

def test_featurize_finance_4():
    assert featurize_finance(1000000, 100000) == [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

def test_featurize_finance_5():
    assert featurize_finance(5000000, 100000) == [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

def test_featurize_finance_6():
    assert featurize_finance(10000000, 100000) == [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

def test_featurize_finance_7():
    assert featurize_finance(50000000, 100000) == [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]

def test_featurize_finance_8():
    assert featurize_finance(100000000, 100000) == [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]

def test_featurize_finance_9():
    assert featurize_finance(500000000, 100000) == [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

def test_featurize_finance_10():
    assert featurize_finance(1000000000, 100000) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
