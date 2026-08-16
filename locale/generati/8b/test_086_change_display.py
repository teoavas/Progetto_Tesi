from funzione import change_display

def test_change_display_1():
    data = ['0', '1', '2']
    mode = 5
    expected_result = [64, 65, 66]
    assert change_display(data, mode) == expected_result

def test_change_display_2():
    data = ['0', '1', '2']
    mode = 15
    expected_result = [32, 33, 34]
    assert change_display(data, mode) == expected_result

def test_change_display_3():
    data = ['0', '1', '2']
    mode = 20
    expected_result = [data]
    assert change_display(data, mode) == expected_result

def test_change_display_4():
    data = ['0', '1', '2']
    mode = 21
    expected_result = [data]
    assert change_display(data, mode) == expected_result

def test_change_display_5():
    data = ['0', '1', '2']
    mode = 10
    expected_result = [64, 65, 66]
    assert change_display(data, mode) == expected_result

def test_change_display_6():
    data = ['0', '1', '2']
    mode = 11
    expected_result = [32, 33, 34]
    assert change_display(data, mode) == expected_result

def test_change_display_7():
    data = ['0', '1', '2']
    mode = 6
    expected_result = [64, 65, 66, 67, 68]
    assert change_display(data, mode) == expected_result

def test_change_display_8():
    data = ['0', '1', '2']
    mode = 16
    expected_result = [32, 33, 34, 35, 36]
    assert change_display(data, mode) == expected_result
