from funzione import diffsents

def test_diffsents_1():
    assert diffsents("abc", "abcd") == (0, 2, 0, 3)

def test_diffsents_2():
    assert diffsents("", "") == (-1, -1, -1, -1)

def test_diffsents_3():
    assert diffsents("a", "b") == (0, 0, 0, 0)

def test_diffsents_4():
    assert diffsents("abc", "") == (0, 2, 0, 0)

def test_diffsents_5():
    assert diffsents("", "abc") == (0, 0, 0, 2)

def test_diffsents_6():
    assert diffsents("ab", "cd") == (1, 1, 1, 1)

def test_diffsents_7():
    assert diffsents("abcd", "abcd") == (-1, -1, -1, -1)
