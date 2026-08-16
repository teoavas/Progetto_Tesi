import pytest

def test_locate_alignment_1():
    assert locate_alignment("ATCG", "ACGT", 0) == [0, 2]

def test_locate_alignment_2():
    assert locate_alignment("ATCG", "ACGT", 3) == [4]

def test_locate_alignment_3():
    assert locate_alignment("ATCG", "ACGT", 5) == []

def test_locate_alignment_4():
    assert locate_alignment("ATCG", "ACGT", 6, resMatch=True) == [0, 2]

def test_locate_alignment_5():
    assert locate_alignment("ATCG", "ACGT", 7) == []

def test_locate_alignment_6():
    assert locate_alignment("ATCG", "ACGT", 8, resMatch=False) == []
