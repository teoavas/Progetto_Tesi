from funzione import longestNonWildcardSubsequence

def test_longestNonWildcardSubsequence_1():
    opCodes = [["A", "B", "*"], ["C", "*", "D"]]
    mask = None
    start, end, result = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 0 and end == 2 and result == '***'

def test_longestNonWildcardSubsequence_2():
    opCodes = [["A", "B"], ["C", "D"]]
    mask = None
    start, end, result = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 0 and end == 1 and result == '11'

def test_longestNonWildcardSubsequence_3():
    opCodes = [["A", "*"], ["*", "B"]]
    mask = None
    start, end, result = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 0 and end == 1 and result == '**'

def test_longestNonWildcardSubsequence_4():
    opCodes = [["A", "B"], ["C", "*"]]
    mask = None
    start, end, result = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 0 and end == 1 and result == '11'

def test_longestNonWildcardSubsequence_5():
    opCodes = [["A", "B"], ["C", "D"]]
    mask = None
    start, end, result = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 0 and end == 1 and result == '11'

def test_longestNonWildcardSubsequence_6():
    opCodes = [["A", "*"], ["*", "B"]]
    mask = None
    start, end, result = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 0 and end == 1 and result == '**'

def test_longestNonWildcardSubsequence_7():
    opCodes = [["A", "B"], ["C", "*"]]
    mask = '11'
    start, end, result = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 0 and end == 1 and result == '11'

def test_longestNonWildcardSubsequence_8():
    opCodes = [["A", "B"], ["C", "*"]]
    mask = None
    start, end, result = longestNonWildcardSubsequence(opCodes, mask)
    assert start == 0 and end == 1 and result == '11'
