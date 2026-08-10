from funzione import calc_query_pos_from_cigar
import re

def test_calc_query_pos_from_cigar_1():
    cigar = '10M5D10M'
    strand = True
    assert calc_query_pos_from_cigar(cigar, strand) == (0, 15)

def test_calc_query_pos_from_cigar_2():
    cigar = '10M5D10M'
    strand = False
    assert calc_query_pos_from_cigar(cigar, strand) == (15, 0)

def test_calc_query_pos_from_cigar_3():
    cigar = '10M5D10M'
    strand = True
    assert calc_query_pos_from_cigar(cigar, strand) != (0, 0)

def test_calc_query_pos_from_cigar_4():
    cigar = '10M5D10M'
    strand = True
    assert calc_query_pos_from_cigar(cigar, strand) != (15, 15)

def test_calc_query_pos_from_cigar_5():
    cigar = '10M5D10M'
    strand = True
    assert calc_query_pos_from_cigar(cigar, strand) == (0, 15)

def test_calc_query_pos_from_cigar_6():
    cigar = '10M5D10M'
    strand = False
    assert calc_query_pos_from_cigar(cigar, strand) == (15, 0)

def test_calc_query_pos_from_cigar_7():
    cigar = '10M5D10M'
    strand = True
    assert calc_query_pos_from_cigar(cigar, strand) != (0, 0)

def test_calc_query_pos_from_cigar_8():
    cigar = '10M5D10M'
    strand = True
    assert calc_query_pos_from_cigar(cigar, strand) != (15, 15)
