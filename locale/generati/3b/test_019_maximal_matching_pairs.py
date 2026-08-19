from funzione import maximal_matching_pairs

def test_maximal_matching_pairs_1():
    assert len(maximal_matching_pairs('abcabc')) == 2

def test_maximal_matching_pairs_2():
    assert set((x, y, l) for x, y, l in maximal_matching_pairs('ababab')) == {(0, 0, 3), (4, 4, 3)}

def test_maximal_matching_pairs_3():
    assert len(maximal_matching_pairs('abcde')) == 0

def test_maximal_matching_pairs_4():
    assert set((x, y, l) for x, y, l in maximal_matching_pairs('aaaaaa')) == {(0, 0, 5), (1, 1, 5), (2, 2, 5), (3, 3, 5), (4, 4, 5)}

def test_maximal_matching_pairs_5():
    assert len(maximal_matching_pairs('abc')) == 0

def test_maximal_matching_pairs_6():
    assert set((x, y, l) for x, y, l in maximal_matching_pairs('abab')) == {(0, 1, 2), (1, 2, 2)}

def test_maximal_matching_pairs_7():
    assert len(maximal_matching_pairs('abcabcabc')) == 6
