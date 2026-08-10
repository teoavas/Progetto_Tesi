import pytest
import math

from funzione import bin_search_range

def test_bin_search_range_1():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hi = 8
    lo = 0
    min_r = 3
    max_r = 7
    assert bin_search_range(array, hi, lo, min_r, max_r) == 7

def test_bin_search_range_2():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hi = 8
    lo = 0
    min_r = 10
    max_r = 15
    assert bin_search_range(array, hi, lo, min_r, max_r) == 0

def test_bin_search_range_3():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hi = 8
    lo = 0
    min_r = 1
    max_r = 1
    assert bin_search_range(array, hi, lo, min_r, max_r) == 1

def test_bin_search_range_4():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hi = 8
    lo = 0
    min_r = 9
    max_r = 9
    assert bin_search_range(array, hi, lo, min_r, max_r) == 1

def test_bin_search_range_5():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hi = 8
    lo = 0
    min_r = 1
    max_r = 9
    assert bin_search_range(array, hi, lo, min_r, max_r) == 9

def test_bin_search_range_6():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hi = 8
    lo = 0
    min_r = 0
    max_r = 0
    assert bin_search_range(array, hi, lo, min_r, max_r) == 0

def test_bin_search_range_7():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hi = 8
    lo = 0
    min_r = 10
    max_r = 15
    assert bin_search_range(array, hi, lo, min_r, max_r) == 0
