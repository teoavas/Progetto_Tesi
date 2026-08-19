from funzione import iterative_levenshtein

def test_iterative_levenshtein_1():
    s = "kitten"
    t = "sitting"
    costs = (1, 1, 1)
    H, D, S, I = iterative_levenshtein(s, t, costs)
    assert H == 1
    assert D == 1
    assert S == 3
    assert I == 0

def test_iterative_levenshtein_2():
    s = "hello"
    t = "world"
    costs = (1, 1, 1)
    H, D, S, I = iterative_levenshtein(s, t, costs)
    assert H == 4
    assert D == 0
    assert S == 2
    assert I == 0

def test_iterative_levenshtein_3():
    s = "abcdef"
    t = "abcxyz"
    costs = (1, 1, 1)
    H, D, S, I = iterative_levenshtein(s, t, costs)
    assert H == 2
    assert D == 0
    assert S == 3
    assert I == 0

def test_iterative_levenshtein_4():
    s = "a"
    t = "b"
    costs = (1, 1, 1)
    H, D, S, I = iterative_levenshtein(s, t, costs)
    assert H == 1
    assert D == 0
    assert S == 0
    assert I == 1

def test_iterative_levenshtein_5():
    s = ""
    t = "hello"
    costs = (1, 1, 1)
    H, D, S, I = iterative_levenshtein(s, t, costs)
    assert H == 0
    assert D == 5
    assert S == 0
    assert I == 0

def test_iterative_levenshtein_6():
    s = "hello"
    t = ""
    costs = (1, 1, 1)
    H, D, S, I = iterative_levenshtein(s, t, costs)
    assert H == 5
    assert D == 0
    assert S == 0
    assert I == 0

def test_iterative_levenshtein_7():
    s = "hello"
    t = "hello"
    costs = (1, 1, 1)
    H, D, S, I = iterative_levenshtein(s, t, costs)
    assert H == 0
    assert D == 0
    assert S == 5
    assert I == 0

def test_iterative_levenshtein_8():
    s = "hello"
    t = "helloworld"
    costs = (1, 1, 1)
    H, D, S, I = iterative_levenshtein(s, t, costs)
    assert H == 0
    assert D == 5
    assert S == 4
    assert I == 0
