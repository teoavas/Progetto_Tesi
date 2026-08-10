from funzione import diffsents

def test_diffsents_1():
    sa = "abc"
    sb = "abc"
    assert diffsents(sa, sb) == (0, 2, 0, 2)

def test_diffsents_2():
    sa = "abc"
    sb = "abcd"
    assert diffsents(sa, sb) == (0, 2, 0, 3)

def test_diffsents_3():
    sa = "abcd"
    sb = "abc"
    assert diffsents(sa, sb) == (1, 3, 0, 2)

def test_diffsents_4():
    sa = "abcd"
    sb = "abcde"
    assert diffsents(sa, sb) == (1, 3, 0, 4)

def test_diffsents_5():
    sa = "abcde"
    sb = "abcd"
    assert diffsents(sa, sb) == (1, 4, 0, 3)

def test_diffsents_6():
    sa = "abcde"
    sb = "abcde"
    assert diffsents(sa, sb) == (0, 4, 0, 4)

def test_diffsents_7():
    sa = "abcde"
    sb = "abc"
    assert diffsents(sa, sb) == (1, 4, 0, 2)

def test_diffsents_8():
    sa = "abc"
    sb = "abcde"
    assert diffsents(sa, sb) == (0, 2, 0, 4)
