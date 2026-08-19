import pytest

def test_make_similar_1():
    assert make_similar([1, 2, 3, 4], [1, 3]) == 0.5

def test_make_similar_2():
    assert make_similar([10, 20, 30, 40], [15, 25, 35, 45]) == 0.75

def test_make_similar_3():
    assert make_similar([1, 4, 9, 16], [1, 5, 11, 17]) == 2.5

def test_make_similar_4():
    assert make_similar([7, 14, 23, 42], [7, 13, 21, 41]) == 0.75

def test_make_similar_5():
    assert make_similar([1, 3, 5, 7], [2, 4, 6, 8]) == 0.25

def test_make_similar_6():
    assert make_similar([10, 20, 30, 40], [15, 25, 35, 45]) == 1.0

def test_make_similar_7():
    assert make_similar([1, 2, 3, 4], [5, 6, 7, 8]) == 0.75

def test_make_similar_8():
    assert make_similar([], []) == 0
