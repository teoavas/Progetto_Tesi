from funzione import bin_search_range
import math

def test_bin_search_range_1():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 1
    max_r = 4
    assert bin_search_range(array, hi, lo, min_r, max_r) == 6

def test_bin_search_range_2():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 1
    max_r = 10
    assert bin_search_range(array, hi, lo, min_r, max_r) == 6

def test_bin_search_range_3():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 10
    max_r = 15
    assert bin_search_range(array, hi, lo, min_r, max_r) == 6

def test_bin_search_range_4():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 10
    max_r = 15
    assert bin_search_range(array, hi, lo, min_r, max_r) == 6

def test_bin_search_range_5():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 10
    max_r = 15
    assert bin_search_range(array, hi, lo, min_r, max_r) == 6

def test_bin_search_range_6():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 10
    max_r = 15
    assert bin_search_range(array, hi, lo, min_r, max_r) == 6

def test_bin_search_range_7():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 10
    max_r = 15
    assert bin_search_range(array, hi, lo, min_r, max_r) == 6

def test_bin_search_range_8():
    array = [1, 2, 3, 4, 5]
    hi = len(array) - 1
    lo = 0
    min_r = 10
    max_r = 15
    assert bin_search_range(array, hi, lo, min_r, max_r) == 6
