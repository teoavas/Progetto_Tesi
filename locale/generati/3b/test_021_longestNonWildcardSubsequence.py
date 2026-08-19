from funzione import longestNonWildcardSubsequence

def test_longestNonWildcardSubsequence_1():
    opCodes = ["*", "a", "*", "b"]
    mask = "111"
    assert longestNonWildcardSubsequence(opCodes, mask) == (0, 2, '11')

def test_longestNonWildcardSubsequence_2():
    opCodes = ["a", "b", "*"]
    mask = "1*1"
    assert longestNonWildcardSubsequence(opCodes, mask) == (0, 1, '1*')

def test_longestNonWildcardSubsequence_3():
    opCodes = ["*", "*", "*"]
    mask = "111"
    assert longestNonWildcardSubsequence(opCodes, mask) == (0, 2, '111')

def test_longestNonWildcardSubsequence_4():
    opCodes = ["a", "b", "c"]
    mask = "1*1"
    assert longestNonWildcardSubsequence(opCodes, mask) == (0, 1, '1*')

def test_longestNonWildcardSubsequence_5():
    opCodes = ["*", "*", "*"]
    mask = ""
    assert longestNonWildcardSubsequence(opCodes, mask) == (0, 2, '')

def test_longestNonWildcardSubsequence_6():
    opCodes = ["a", "b", "c"]
    mask = "1*"
    assert longestNonWildcardSubsequence(opCodes, mask) == (0, 1, '1*')

def test_longestNonWildcardSubsequence_7():
    opCodes = ["*", "*", "*"]
    mask = "1*1"
    assert longestNonWildcardSubsequence(opCodes, mask) == (0, 2, '1*1')
