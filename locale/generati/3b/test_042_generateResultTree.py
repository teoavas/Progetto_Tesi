from funzione import generateResultTree

def test_generateResultTree_1():
    assert generateResultTree([[0, 0, 0, 0], [0, 0, 0, 1]]) == [2, 2, 2, 2]

def test_generateResultTree_2():
    assert generateResultTree([[0, 0, 0, 0], [0, 0, 1, 0]]) == [-1, -1, -1, -1]

def test_generateResultTree_3():
    assert generateResultTree([[0, 0, 0, 0], [0, 1, 0, 0]]) == [2, 2, 2, 2]

def test_generateResultTree_4():
    assert generateResultTree([[0, 0, 0, 0], [1, 0, 0, 0]]) == [-1, -1, -1, -1]

def test_generateResultTree_5():
    assert generateResultTree([[0, 0, 0, 0], [0, 0, 0, 1]]) == [2, 2, 2, 2]

def test_generateResultTree_6():
    assert generateResultTree([[0, 0, 0, 0], [0, 0, 1, 1]]) == [-1, -1, -1, -1]

def test_generateResultTree_7():
    assert generateResultTree([[0, 0, 0, 0], [0, 1, 1, 0]]) == [2, 2, 2, 2]

def test_generateResultTree_8():
    assert generateResultTree([[0, 0, 0, 0], [1, 1, 0, 0]]) == [-1, -1, -1, -1]
