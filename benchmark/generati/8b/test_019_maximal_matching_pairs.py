from funzione import maximal_matching_pairs

def test_maximal_matching_pairs_1():
    assert list(maximal_matching_pairs('abc')) == []

def test_maximal_matching_pairs_2():
    assert list(maximal_matching_pairs('abab')) == []

def test_maximal_matching_pairs_3():
    assert list(maximal_matching_pairs('ababa')) == []

def test_maximal_matching_pairs_4():
    assert list(maximal_matching_pairs('abababa')) == []

def test_maximal_matching_pairs_5():
    assert list(maximal_matching_pairs('abcabc')) == []

def test_maximal_matching_pairs_6():
    assert list(maximal_matching_pairs('ababab')) == []

def test_maximal_matching_pairs_7():
    assert list(maximal_matching_pairs('ababababa')) == []

def test_maximal_matching_pairs_8():
    assert list(maximal_matching_pairs('')) == []
