from funzione import getYAxisMinMaxGC

def test_getYAxisMinMaxGC_1():
    LGC = [10, 20, 30]
    RGC = [40, 50, 60]
    assert getYAxisMinMaxGC(LGC, RGC) == (0, 60)

def test_getYAxisMinMaxGC_2():
    LGC = [10, 20, 30]
    RGC = [10, 20, 30]
    assert getYAxisMinMaxGC(LGC, RGC) == (0, 30)

def test_getYAxisMinMaxGC_3():
    LGC = [10, 20, 30]
    RGC = [40, 50, 60]
    assert getYAxisMinMaxGC(LGC, RGC) == (0, 60)

def test_getYAxisMinMaxGC_4():
    LGC = [10, 20, 30]
    RGC = [40, 50, 60]
    assert getYAxisMinMaxGC(LGC, RGC) == (0, 60)

def test_getYAxisMinMaxGC_5():
    LGC = [10, 20, 30]
    RGC = [40, 50, 60]
    assert getYAxisMinMaxGC(LGC, RGC) == (0, 60)

def test_getYAxisMinMaxGC_6():
    LGC = [10, 20, 30]
    RGC = [40, 50, 60]
    assert getYAxisMinMaxGC(LGC, RGC) == (0, 60)

def test_getYAxisMinMaxGC_7():
    LGC = [10, 20, 30]
    RGC = [40, 50, 60]
    assert getYAxisMinMaxGC(LGC, RGC) == (0, 60)

def test_getYAxisMinMaxGC_8():
    LGC = [10, 20, 30]
    RGC = [40, 50, 60]
    assert getYAxisMinMaxGC(LGC, RGC) == (0, 60)

def test_getYAxisMinMaxGC_9():
    LGC = [10, 20, 30]
    RGC = [40, 50, 60]
    assert getYAxisMinMaxGC(LGC, RGC) == (0, 60)

def test_getYAxisMinMaxGC_10():
    LGC = [10, 20, 30]
    RGC = [40, 50, 60]
    assert getYAxisMinMaxGC(LGC, RGC) == (0, 60)
