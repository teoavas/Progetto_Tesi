from funzione import iterative_levenshtein

def test_iterative_levenshtein_1():
    assert iterative_levenshtein("kitten", "sitting") == (3, 2, 1, 1)

def test_iterative_levenshtein_2():
    assert iterative_levenshtein("", "hello") == (5, 0, 0, 0)

def test_iterative_levenshtein_3():
    assert iterative_levenshtein("hello", "") == (0, 5, 0, 0)

def test_iterative_levenshtein_4():
    assert iterative_levenshtein("hello", "hello") == (0, 0, 0, 0)

def test_iterative_levenshtein_5():
    assert iterative_levenshtein("abc", "def") == (3, 3, 0, 0)

def test_iterative_levenshtein_6():
    assert iterative_levenshtein("abcdef", "abcxyz") == (3, 3, 0, 2)

def test_iterative_levenshtein_7():
    assert iterative_levenshtein("abcdef", "abc") == (3, 3, 0, 0)

def test_iterative_levenshtein_8():
    assert iterative_levenshtein("abc", "abcdef") == (3, 0, 0, 3)
