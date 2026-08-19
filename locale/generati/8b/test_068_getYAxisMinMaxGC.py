from funzione import getYAxisMinMaxGC

def test_getYAxisMinMaxGC_1():
    LGC = [10, 20, 30]
    RGC = [40, 50, 60]
    min_max = getYAxisMinMaxGC(LGC, RGC)
    assert min_max == (0, 60)

def test_getYAxisMinMaxGC_2():
    LGC = [100, 200, 300]
    RGC = [400, 500, 600]
    min_max = getYAxisMinMaxGC(LGC, RGC)
    assert min_max == (0, 600)

def test_getYAxisMinMaxGC_3():
    LGC = [-10, -20, -30]
    RGC = [-40, -50, -60]
    min_max = getYAxisMinMaxGC(LGC, RGC)
    assert min_max == (-100, -60)

def test_getYAxisMinMaxGC_4():
    LGC = [0, 0, 0]
    RGC = [0, 0, 0]
    min_max = getYAxisMinMaxGC(LGC, RGC)
    assert min_max == (0, 50)

def test_getYAxisMinMaxGC_5():
    LGC = [1000, 2000, 3000]
    RGC = [4000, 5000, 6000]
    min_max = getYAxisMinMaxGC(LGC, RGC)
    assert min_max == (0, 450)

def test_getYAxisMinMaxGC_6():
    LGC = [-1000, -2000, -3000]
    RGC = [-4000, -5000, -6000]
    min_max = getYAxisMinMaxGC(LGC, RGC)
    assert min_max == (-400, 50)

def test_getYAxisMinMaxGC_7():
    LGC = [10000, 20000, 30000]
    RGC = [40000, 50000, 60000]
    min_max = getYAxisMinMaxGC(LGC, RGC)
    assert min_max == (0, 450)

def test_getYAxisMinMaxGC_8():
    LGC = [-100000, -200000, -300000]
    RGC = [-400000, -500000, -600000]
    min_max = getYAxisMinMaxGC(LGC, RGC)
    assert min_max == (-400, 50)
