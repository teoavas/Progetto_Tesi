import pytest
from funzione import usage_bound

def test_usage_bound_1():
    assert usage_bound([100, 200, 300], 3, 'single') > 0

def test_usage_bound_2():
    assert usage_bound([500, 600, 700], 4, 'raid0') == 250

def test_usage_bound_3():
    assert usage_bound([800, 900, 1000], 5, 'raid1') == 400

def test_usage_bound_4():
    assert usage_bound([1200, 1300, 1400], 6, 'raid10') == 600

def test_usage_bound_5():
    assert usage_bound([1500, 1600, 1700], 7, 'raid5') > 0

def test_usage_bound_6():
    assert usage_bound([1800, 1900, 2000], 8, 'raid6') == 800

def test_usage_bound_7():
    assert usage_bound([2200, 2300, 2400], 9, 'raid1') > 0
