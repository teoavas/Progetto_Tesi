import pytest

def test_cigar_prefix_length_1():
    assert cigar_prefix_length("M", 10) == (10, 0)
    assert cigar_prefix_length("X", 10) == (10, 5)
    assert cigar_prefix_length("=", 10) == (10, 6)

def test_cigar_prefix_length_2():
    assert cigar_prefix_length("D", 10) == (10, 7)
    assert cigar_prefix_length("I", 10) == (10, 8)
    assert cigar_prefix_length("N", 10) == (10, 0)

def test_cigar_prefix_length_3():
    assert cigar_prefix_length("S", 10) == (10, 9)

def test_cigar_prefix_length_4():
    assert cigar_prefix_length("H", 10) == (10, 11)
    assert cigar_prefix_length("R", 10) == (10, 12)

def test_cigar_prefix_length_5():
    assert cigar_prefix_length("K", 10) == (10, 13)

def test_cigar_prefix_length_6():
    assert cigar_prefix_length("M", 10) == (10, 0)
    assert cigar_prefix_length("X", 10) == (10, 5)
    assert cigar_prefix_length("=", 10) == (10, 6)
