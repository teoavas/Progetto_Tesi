from funzione import maximal_matching_pairs

def test_maximal_matching_pairs_1():
    string = "abcde"
    result = list(maximal_matching_pairs(string))
    assert len(result) == 0

def test_maximal_matching_pairs_2():
    string = "ababa"
    result = list(maximal_matching_pairs(string))
    assert len(result) == 3
    assert (0, 1, 2) in result and (1, 2, 2) in result and (2, 3, 2) in result

def test_maximal_matching_pairs_3():
    string = "abccba"
    result = list(maximal_matching_pairs(string))
    assert len(result) == 4
    assert (0, 1, 2) in result and (1, 2, 2) in result and (2, 3, 2) in result and (3, 4, 2) in result

def test_maximal_matching_pairs_4():
    string = "abcde"
    result = list(maximal_matching_pairs(string))
    assert len(result) == 0

def test_maximal_matching_pairs_5():
    string = "aaaaa"
    result = list(maximal_matching_pairs(string))
    assert len(result) == 1
    assert (0, 1, 4) in result

def test_maximal_matching_pairs_6():
    string = "ababab"
    result = list(maximal_matching_pairs(string))
    assert len(result) == 3
    assert (0, 1, 2) in result and (1, 2, 2) in result and (2, 3, 2) in result

def test_maximal_matching_pairs_7():
    string = "abcdef"
    result = list(maximal_matching_pairs(string))
    assert len(result) == 0
