from funzione import calc_query_pos_from_cigar
import re

def test_calc_query_pos_from_cigar_1():
    assert calc_query_pos_from_cigar('10M', True) == (0, 10)

def test_calc_query_pos_from_cigar_2():
    assert calc_query_pos_from_cigar('20H10M', False) == (10, 20)

def test_calc_query_pos_from_cigar_3():
    assert calc_query_pos_from_cigar('30I25X', True) == (0, 25)

def test_calc_query_pos_from_cigar_4():
    assert calc_query_pos_from_cigar('40S15H', False) == (15, 40)

def test_calc_query_pos_from_cigar_5():
    assert calc_query_pos_from_cigar('50M20I10X', True) == (0, 30)

def test_calc_query_pos_from_cigar_6():
    assert calc_query_pos_from_cigar('60H25S15M', False) == (15, 75)

def test_calc_query_pos_from_cigar_7():
    assert calc_query_pos_from_cigar('70I20X10M', True) == (0, 30)
