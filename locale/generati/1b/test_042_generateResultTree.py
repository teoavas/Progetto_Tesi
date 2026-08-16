import pytest

def test_generateResultTree_1():
    assert generateResultTree([["A", "2"], ["K", "3"]]) == [0, 0, -1]

def test_generateResultTree_2():
    assert generateResultTree([["Q", "4"], ["J", "5"]]) == [0, 0, -1]

def test_generateResultTree_3():
    assert generateResultTree([["10", "9"], ["8", "7"]]) == [0, 0, -1]

def test_generateResultTree_4():
    assert generateResultTree([["5", "4"], ["3", "2"]]) == [0, 0, -1]

def test_generateResultTree_5():
    assert generateResultTree([["A", "K"], ["Q", "J"]]) == [0, 0, -1]

def test_generateResultTree_6():
    assert generateResultTree([["10", "9"], ["8", "7"], ["3", "2"]]) == [0, 0, -1]

def test_generateResultTree_7():
    assert generateResultTree([["5", "4"], ["3", "2"], ["A", "K"]]) == [0, 0, -1]

def test_generateResultTree_8():
    assert generateResultTree([["10", "9"], ["8", "7"], ["Q", "J"]]) == [0, 0, -1]
