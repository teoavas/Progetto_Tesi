import re
from pytest import raises

def test_calc_query_pos_from_cigar_1():
    cigar = "12H3M4I5"
    expected = (15, 20)
    assert calc_query_pos_from_cigar(cigar) == expected

def test_calc_query_pos_from_cigar_2():
    cigar = "10S13M14"
    expected = (23, 27)
    assert calc_query_pos_from_cigar(cigar) == expected

def test_calc_query_pos_from_cigar_3():
    cigar = "5H6I7"
    expected = (11, 18)
    assert calc_query_pos_from_cigar(cigar) == expected

def test_calc_query_pos_from_cigar_4():
    cigar = "8M9X10"
    expected = (17, 29)
    assert calc_query_pos_from_cigar(cigar) == expected

def test_calc_query_pos_from_cigar_5():
    cigar = "2S3I4H5"
    expected = (6, 14)
    assert calc_query_pos_from_cigar(cigar) == expected

def test_calc_query_pos_from_cigar_6():
    cigar = "1M2X3S4"
    expected = (3, 8)
    assert calc_query_pos_from_cigar(cigar) == expected

def test_calc_query_pos_from_cigar_7():
    cigar = "9H10I11"
    expected = (19, 30)
    assert calc_query_pos_from_cigar(cigar) == expected

def test_calc_query_pos_from_cigar_8():
    cigar = "3S4M5X6"
    expected = (13, 25)
    assert calc_query_pos_from_cigar(cigar) == expected
