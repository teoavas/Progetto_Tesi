import pytest

def test_maximal_matching_pairs_1():
    pairs = list(maximal_matching_pairs("abc"))
    assert len(pairs) > 0 and all(0 <= pair[2] for pair in pairs)

def test_maximal_matching_pairs_2():
    pairs = list(maximal_matching_pairs("abcd"))
    assert len(pairs) > 0 and all(0 <= pair[2] for pair in pairs)

def test_maximal_matching_pairs_3():
    pairs = list(maximal_matching_pairs("abcde"))
    assert len(pairs) > 0 and all(0 <= pair[2] for pair in pairs)

def test_maximal_matching_pairs_4():
    pairs = list(maximal_matching_pairs("abccba"))
    assert len(pairs) == 1

def test_maximal_matching_pairs_5():
    pairs = list(maximal_matching_pairs("abcdcba"))
    assert len(pairs) > 0 and all(0 <= pair[2] for pair in pairs)

def test_maximal_matching_pairs_6():
    pairs = list(maximal_matching_pairs("abcdeef"))
    assert len(pairs) == 1

def test_maximal_matching_pairs_7():
    pairs = list(maximal_matching_pairs("abccbaa"))
    assert len(pairs) > 0 and all(0 <= pair[2] for pair in pairs)

def test_maximal_matching_pairs_8():
    pairs = list(maximal_matching_pairs("abcdcbaaa"))
    assert len(pairs) > 0 and all(0 <= pair[2] for pair in pairs)
