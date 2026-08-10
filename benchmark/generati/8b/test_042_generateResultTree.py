from funzione import generateResultTree

def test_generateResultTree_1():
    cards = [[1, 2], [3, 4], [5, 6]]
    assert generateResultTree(cards) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_generateResultTree_2():
    cards = [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert generateResultTree(cards) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_generateResultTree_3():
    cards = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    assert generateResultTree(cards) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_generateResultTree_4():
    cards = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
    assert generateResultTree(cards) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_generateResultTree_5():
    cards = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]]
    assert generateResultTree(cards) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_generateResultTree_6():
    cards = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]]
    assert generateResultTree(cards) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_generateResultTree_7():
    cards = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18]]
    assert generateResultTree(cards) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
