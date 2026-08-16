from funzione import change_display

def test_change_display_1():
    assert change_display([1,2,3], 5) == [65, 66, 67]

def test_change_display_2():
    assert change_display([1,2,3], 10) == [32, 34, 36]

def test_change_display_3():
    assert change_display([1,2,3], 15) == [32, 64, 96]

def test_change_display_4():
    assert change_display([1,2,3], 25) == [32, 64, 96]

def test_change_display_5():
    assert change_display([1,2,3], 0) == [1, 2, 3]

def test_change_display_6():
    assert change_display([1,2,3], -1) == [1, 2, 3]

def test_change_display_7():
    assert change_display([1,2,3], 21) == [1, 2, 3]

def test_change_display_8():
    assert change_display([1,2,3], 5.5) == [1, 2, 3]
