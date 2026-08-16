from funzione import getYAxisMinMaxGC

def test_getYAxisMinMaxGC_1():
    assert getYAxisMinMaxGC([10, 20], [30, 40]) == (-50, 50)

def test_getYAxisMinMaxGC_2():
    assert getYAxisMinMaxGC([1000, 2000], [3000, 4000]) == (0, 400)

def test_getYAxisMinMaxGC_3():
    assert getYAxisMinMaxGC([-10, -20], [-30, -40]) == (-50, 50)

def test_getYAxisMinMaxGC_4():
    assert getYAxisMinMaxGC([1.5, 2.7], [3.9, 4.1]) == (0, 400)

def test_getYAxisMinMaxGC_5():
    assert getYAxisMinMaxGC([100, 200], [50, 60]) == (-50, 150)

def test_getYAxisMinMaxGC_6():
    assert getYAxisMinMaxGC([-10, -20], [-30, -40]) == (0, 400)

def test_getYAxisMinMaxGC_7():
    assert getYAxisMinMaxGC([1.5, 2.7], [3.9, 4.1]) == (-50, 150)
