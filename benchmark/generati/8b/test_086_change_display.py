from funzione import change_display

def test_change_display_1():
    data = ['1', '2', '3', '4', '5']
    assert change_display(data, 1) == [65, 66, 67, 68, 69]

def test_change_display_2():
    data = ['1', '2', '3', '4', '5']
    assert change_display(data, 6) == [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

def test_change_display_3():
    data = ['1', '2', '3', '4', '5']
    assert change_display(data, 11) == [65, 66, 67, 68, 69, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]

def test_change_display_4():
    data = ['1', '2', '3', '4', '5']
    assert change_display(data, 20) == [65, 66, 67, 68, 69, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]

def test_change_display_5():
    data = ['1', '2', '3', '4', '5']
    assert change_display(data, 0) == [1, 2, 3, 4, 5]

def test_change_display_6():
    data = ['1', '2', '3', '4', '5']
    assert change_display(data, 21) == [1, 2, 3, 4, 5]

def test_change_display_7():
    data = ['1', '2', '3', '4', '5']
    assert change_display(data, 5) == [65, 66, 67, 68, 69]

def test_change_display_8():
    data = ['1', '2', '3', '4', '5']
    assert change_display(data, 15) == [65, 66, 67, 68, 69, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
