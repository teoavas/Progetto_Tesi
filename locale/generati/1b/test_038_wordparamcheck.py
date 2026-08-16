import pytest

def test_wordparamcheck_1():
    givenparams = ["a", "b"]
    expectedparams = ["a", "b", "more", False, 2, ["a", "b"]]
    output = wordparamcheck(givenparams, expectedparams)
    assert output[0] == True
    assert output[1] == 0
    assert output[2] == "b"
    assert output[3] == True
    assert output[4] == 2
    assert output[5] == ["a", "b"]

def test_wordparamcheck_2():
    givenparams = ["a"]
    expectedparams = ["a", "more", False, 1, 0, ["NULL"]]
    output = wordparamcheck(givenparams, expectedparams)
    assert output[0] == True
    assert output[1] == 0
    assert output[2] == "a"
    assert output[3] == True
    assert output[4] == 1
    assert output[5] == ["NULL"]

def test_wordparamcheck_3():
    givenparams = ["a", "b"]
    expectedparams = ["a", "b", "none", False, 2, ["a", "b"]]
    output = wordparamcheck(givenparams, expectedparams)
    assert output[0] == True
    assert output[1] == 0
    assert output[2] == "b"
    assert output[3] == True
    assert output[4] == 2
    assert output[5] == ["a", "b"]

def test_wordparamcheck_4():
    givenparams = ["a"]
    expectedparams = ["a", "optional", False, 1, 0, ["NULL"]]
    output = wordparamcheck(givenparams, expectedparams)
    assert output[0] == True
    assert output[1] == 0
    assert output[2] == "a"
    assert output[3] == True
    assert output[4] == 1
    assert output[5] == ["NULL"]

def test_wordparamcheck_5():
    givenparams = ["a", "b"]
    expectedparams = ["a", "optional", False, 0, 0, ["NULL"]]
    output = wordparamcheck(givenparams, expectedparams)
    assert output[0] == True
    assert output[1] == 0
    assert output[2] == "a"
    assert output[3] == True
    assert output[4] == 0
    assert output[5] == ["NULL"]

def test_wordparamcheck_6():
    givenparams = ["a"]
    expectedparams = ["a", "skip", False, 1, 0, ["NULL"]]
    output = wordparamcheck(givenparams, expectedparams)
    assert output[0] == True
    assert output[1] == 0
    assert output[2] == "a"
    assert output[3] == True
    assert output[4] == 1
    assert output[5] == ["NULL"]

def test_wordparamcheck_7():
    givenparams = ["a", "b"]
    expectedparams = ["a", "optional", False, 0, 0, ["NULL"]]
    output = wordparamcheck(givenparams, expectedparams)
    assert output[0] == True
    assert output[1] == 0
    assert output[2] == "a"
    assert output[3] == True
    assert output[4] == 0
    assert output[5] == ["NULL"]

def test_wordparamcheck_8():
    givenparams = ["a", "b"]
    expectedparams = ["a", "optional", False, 1, 0, ["NULL"]]
    output = wordparamcheck(givenparams, expectedparams)
    assert output[0] == True
    assert output[1] == 1
    assert output[2] == "b"
    assert output[3] == True
    assert output[4] == 1
    assert output[5] == ["NULL"]
