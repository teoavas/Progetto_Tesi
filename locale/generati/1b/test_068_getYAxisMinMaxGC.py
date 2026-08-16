import pytest

def test_getYAxisMinMaxGC_1():
    assert getYAxisMinMaxGC(100, 200) == (50, 150)

def test_getYAxisMinMaxGC_2():
    assert getYAxisMinMaxGC(-10, -20) == (-100, -50)

def test_getYAxisMinMaxGC_3():
    assert getYAxisMinMaxGC(300, 400) == (350, 450)

def test_getYAxisMinMaxGC_4():
    assert getYAxisMinMaxGC(-500, -600) == (-100, -50)

def test_getYAxisMinMaxGC_5():
    assert getYAxisMinMaxGC(700, 800) == (200, 300)

def test_getYAxisMinMaxGC_6():
    assert getYAxisMinMaxGC(-900, -1000) == (-250, -100)

def test_getYAxisMinMaxGC_7():
    assert getYAxisMinMaxGC(1100, 1200) == (400, 450)
