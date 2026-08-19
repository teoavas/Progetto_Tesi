import math
from funzione import bin_search_range

def test_bin_search_range_1():
    array = [1, 2, 3, 4, 5]
    lo = 0
    hi = len(array) - 1
    min_r = 2
    max_r = 4
    assert bin_search_range(array, hi, lo, min_r, max_r) == 3

def test_bin_search_range_2():
    array = [10, 20, 30, 40, 50]
    lo = 0
    hi = len(array) - 1
    min_r = 15
    max_r = 25
    assert bin_search_range(array, hi, lo, min_r, max_r) == 5

def test_bin_search_range_3():
    array = [100, 200, 300, 400, 500]
    lo = 0
    hi = len(array) - 1
    min_r = 150
    max_r = 250
    assert bin_search_range(array, hi, lo, min_r, max_r) == 5

def test_bin_search_range_4():
    array = [1000, 2000, 3000, 4000, 5000]
    lo = 0
    hi = len(array) - 1
    min_r = 1500
    max_r = 2500
    assert bin_search_range(array, hi, lo, min_r, max_r) == 5

def test_bin_search_range_5():
    array = [10000, 20000, 30000, 40000, 50000]
    lo = 0
    hi = len(array) - 1
    min_r = 15000
    max_r = 25000
    assert bin_search_range(array, hi, lo, min_r, max_r) == 5

def test_bin_search_range_6():
    array = [100000, 200000, 300000, 400000, 500000]
    lo = 0
    hi = len(array) - 1
    min_r = 150000
    max_r = 250000
    assert bin_search_range(array, hi, lo, min_r, max_r) == 5

def test_bin_search_range_7():
    array = [1000000, 2000000, 3000000, 4000000, 5000000]
    lo = 0
    hi = len(array) - 1
    min_r = 1500000
    max_r = 2500000
    assert bin_search_range(array, hi, lo, min_r, max_r) == 5

def test_bin_search_range_8():
    array = [10000000, 20000000, 30000000, 40000000, 50000000]
    lo = 0
    hi = len(array) - 1
    min_r = 15000000
    max_r = 25000000
    assert bin_search_range(array, hi, lo, min_r, max_r) == 5
