import pytest
import math

from funzione import bin_search_range

def test_bin_search_range_1():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 2
    max_r = 4
    assert bin_search_range(array, hi, lo, min_r, max_r) == 3

def test_bin_search_range_2():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 6
    max_r = 8
    assert bin_search_range(array, hi, lo, min_r, max_r) == 0

def test_bin_search_range_3():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 1
    max_r = 6
    assert bin_search_range(array, hi, lo, min_r, max_r) == 5

def test_bin_search_range_4():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 6
    max_r = 8
    assert bin_search_range(array, hi, lo, min_r, max_r) == 0

def test_bin_search_range_5():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 6
    max_r = 8
    assert bin_search_range(array, hi, lo, min_r, max_r) == 0

def test_bin_search_range_6():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 1
    max_r = 6
    assert bin_search_range(array, hi, lo, min_r, max_r) == 5

def test_bin_search_range_7():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 6
    max_r = 8
    assert bin_search_range(array, hi, lo, min_r, max_r) == 0

def test_bin_search_range_8():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 6
    max_r = 8
    assert bin_search_range(array, hi, lo, min_r, max_r) == 0
