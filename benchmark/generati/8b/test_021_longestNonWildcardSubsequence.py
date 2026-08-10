from funzione import longestNonWildcardSubsequence

def test_longestNonWildcardSubsequence_1():
    opCodes = [["a", "b", "c"], ["d", "e", "f"]]
    assert longestNonWildcardSubsequence(opCodes) == (0, 2, "1"*3)

def test_longestNonWildcardSubsequence_2():
    opCodes = [["a", "b", "c"], ["d", "e", "f"]]
    mask = "1"*3
    assert longestNonWildcardSubsequence(opCodes, mask) == (0, 2, "1"*3)

def test_longestNonWildcardSubsequence_3():
    opCodes = [["a", "b", "c"], ["d", "e", "f"]]
    assert longestNonWildcardSubsequence(opCodes, "0"*3) == (1, 2, "1"*3)

def test_longestNonWildcardSubsequence_4():
    opCodes = [["a", "b", "c"], ["d", "e", "f"]]
    mask = "0"*3
    assert longestNonWildcardSubsequence(opCodes, mask) == (1, 2, "1"*3)

def test_longestNonWildcardSubsequence_5():
    opCodes = [["a", "b", "c"], ["d", "e", "f"]]
    mask = "1"*3
    assert longestNonWildcardSubsequence(opCodes, mask) == (0, 2, "1"*3)

def test_longestNonWildcardSubsequence_6():
    opCodes = [["a", "b", "c"], ["d", "e", "f"]]
    mask = "0"*3
    assert longestNonWildcardSubsequence(opCodes, mask) == (1, 2, "1"*3)

def test_longestNonWildcardSubsequence_7():
    opCodes = [["a", "b", "c"], ["d", "e", "f"]]
    mask = "1"*3
    assert longestNonWildcardSubsequence(opCodes, mask) == (0, 2, "1"*3)

def test_longestNonWildcardSubsequence_8():
    opCodes = [["a", "b", "c"], ["d", "e", "f"]]
    mask = "0"*3
    assert longestNonWildcardSubsequence(opCodes, mask) == (1, 2, "1"*3)
