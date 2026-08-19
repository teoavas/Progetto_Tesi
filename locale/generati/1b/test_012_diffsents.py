import pytest

def test_diffsents_1():
    assert diffsents("abc", "abcd") == (0, 2, 3, 4)

def test_diffsents_2():
    assert diffsents("xyz", "yza") == (0, 5, 6, 7)

def test_diffsents_3():
    assert diffsents("aaa", "aab") == (1, 2, 3, 4)

def test_diffsents_4():
    assert diffsents("abc", "abca") == (0, 2, 3, 5)

def test_diffsents_5():
    assert diffsents("abcd", "acbd") == (0, 1, 2, 3)

def test_diffsents_6():
    assert diffsents("xyz", "xzy") == (0, 4, 5, 6)
