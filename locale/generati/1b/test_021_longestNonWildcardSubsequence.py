import pytest

def test_longestNonWildcardSubsequence_1():
    opCodes = ["*"]
    mask = "1"*len(opCodes[0])
    start, end, subseq = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 1
    assert end == 2
    assert subseq == "*"

def test_longestNonWildcardSubsequence_2():
    opCodes = ["*"]
    mask = "11"
    with pytest.raises(ValueError):
        longestNonWildcardSubsequence(opCodes, mask)

def test_longestNonWildcardSubsequence_3():
    opCodes = ["*", "*"]
    mask = "1"*len(opCodes[0])
    start, end, subseq = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 2
    assert end == 4
    assert subseq == "*"

def test_longestNonWildcardSubsequence_4():
    opCodes = ["*", "*", "*"]
    mask = "1"*len(opCodes[0])
    start, end, subseq = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 3
    assert end == 6
    assert subseq == "*"

def test_longestNonWildcardSubsequence_5():
    opCodes = ["*", "*", "1"]
    mask = "11"
    with pytest.raises(ValueError):
        longestNonWildcardSubsequence(opCodes, mask)

def test_longestNonWildcardSubsequence_6():
    opCodes = ["*"]
    mask = "*"
    start, end, subseq = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 1
    assert end == 2
    assert subseq == "*"

def test_longestNonWildcardSubsequence_7():
    opCodes = ["*", "*", "1"]
    mask = "11"
    with pytest.raises(ValueError):
        longestNonWildcardSubsequence(opCodes, mask)

def test_longestNonWildcardSubsequence_8():
    opCodes = ["*"]
    mask = "*"
    start, end, subseq = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 1
    assert end == 2
    assert subseq == "*"

def test_longestNonWildcardSubsequence_9():
    opCodes = ["*", "*", "1"]
    mask = "11"
    with pytest.raises(ValueError):
        longestNonWildcardSubsequence(opCodes, mask)
