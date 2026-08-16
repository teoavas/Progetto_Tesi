import pytest

def test_featurize_finance_1():
    assert featurize_finance(100000, 500000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_featurize_finance_2():
    assert featurize_finance(200000, 700000) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def test_featurize_finance_3():
    assert featurize_finance(300000, 900000) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_featurize_finance_4():
    assert featurize_finance(400000, 1.2 * 10**6) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def test_featurize_finance_5():
    assert featurize_finance(500000, 1.5 * 10**7) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_featurize_finance_6():
    assert featurize_finance(600000, 2 * 10**8) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def test_featurize_finance_7():
    assert featurize_finance(700000, 3 * 10**9) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
