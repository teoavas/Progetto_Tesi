from funzione import iterative_levenshtein

def test_iterative_levenshtein_1():
    assert iterative_levenshtein('abc', 'def') == (0, 3, 1, 2)

def test_iterative_levenshtein_2():
    assert iterative_levenshtein('', 'abc') == (0, 3, 0, 3)
    assert iterative_levenshtein('abc', '') == (3, 0, 3, 0)

def test_iterative_levenshtein_3():
    assert iterative_levenshtein('abc', 'abc') == (0, 0, 0, 0)

def test_iterative_levenshtein_4():
    assert iterative_levenshtein('abca', 'bcb') == (1, 2, 1, 2)

def test_iterative_levenshtein_5():
    assert iterative_levenshtein('abc', 'abcd') == (0, 3, 1, 4)

def test_iterative_levenshtein_6():
    assert iterative_levenshtein('abcdef', 'z') == (7, 0, 7, 0)
