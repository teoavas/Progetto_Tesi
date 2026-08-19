from funzione import calc_query_pos_from_cigar
import re

def test_calc_query_pos_from_cigar_1():
    cigar = "10M5D"
    strand = True
    expected_result = (0, 15)
    assert calc_query_pos_from_cigar(cigar, strand) == expected_result

def test_calc_query_pos_from_cigar_2():
    cigar = "10H5S"
    strand = False
    expected_result = (10, 15)
    assert calc_query_pos_from_cigar(cigar, strand) == expected_result

def test_calc_query_pos_from_cigar_3():
    cigar = "10M5I"
    strand = True
    expected_result = (0, 15)
    assert calc_query_pos_from_cigar(cigar, strand) == expected_result

def test_calc_query_pos_from_cigar_4():
    cigar = "10X5D"
    strand = False
    expected_result = (10, 15)
    assert calc_query_pos_from_cigar(cigar, strand) == expected_result

def test_calc_query_pos_from_cigar_5():
    cigar = ""
    strand = True
    expected_result = (0, 0)
    assert calc_query_pos_from_cigar(cigar, strand) == expected_result

def test_calc_query_pos_from_cigar_6():
    cigar = "10M"
    strand = False
    expected_result = (10, 10)
    assert calc_query_pos_from_cigar(cigar, strand) == expected_result

def test_calc_query_pos_from_cigar_7():
    cigar = "10I5D"
    strand = True
    expected_result = (0, 15)
    assert calc_query_pos_from_cigar(cigar, strand) == expected_result
