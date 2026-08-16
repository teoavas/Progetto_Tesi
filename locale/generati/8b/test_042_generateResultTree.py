```python
from funzione import generateResultTree

def test_generateResultTree_1():
    cards = [[{'suit': 'hearts', 'value': 5}, {'suit': 'diamonds', 'value': 3}, {'suit': 'clubs', 'value': 8}, {'suit': 'spades', 'value': 2}], 
             [{'suit': 'hearts', 'value': 9}, {'suit': 'diamonds', 'value': 1}, {'suit': 'clubs', 'value': 7}, {'suit': 'spades', 'value': 4}]]
    assert generateResultTree(cards) == [0, 0]

def test_generateResultTree_2():
    cards = [[{'suit': 'hearts', 'value': 5}, {'suit': 'diamonds', 'value': 3}, {'suit': 'clubs', 'value': 8}, {'suit': 'spades', 'value': 2}], 
             [{'suit': 'hearts', 'value': 9}, {'suit': 'diamonds', 'value': 1}, {'suit': 'clubs', 'value': 7}, {'suit': 'spades', 'value': 4}],
             [{'suit': 'hearts', 'value': 5}, {'suit': 'diamonds', 'value': 3}, {'suit': 'clubs', 'value': 8}, {'suit': 'spades', 'value': 2}]]
    assert generateResultTree(cards) == [0, 0, 0]

def test_generateResultTree_3():
    cards = [[{'suit': 'hearts', 'value': 5}, {'suit': 'diamonds', 'value': 3}, {'suit': 'clubs', 'value': 8}, {'suit': 'spades', 'value': 2}], 
             [{'suit': 'hearts', 'value': 9}, {'suit': 'diamonds', 'value': 1}, {'suit': 'clubs', 'value': 7}, {'suit': 'spades', 'value': 4}],
             [{'suit': 'hearts', 'value': 5}, {'suit': 'diamonds', 'value': 3}, {'suit': 'clubs', 'value': 8}, {'suit': 'spades', 'value': 2}],
             [{'suit': 'hearts', 'value': 9}, {'suit': 'diamonds', 'value': 1}, {'suit': 'clubs', 'value': 7}, {'suit': 'spades', 'value': 4}]]
    assert generateResultTree(cards) == [0, 0, 0, 0]

def test_generateResultTree_4():
    cards = [[{'suit': 'hearts', 'value': 5}, {'suit': 'diamonds', 'value': 3}, {'suit': 'clubs', 'value': 8}, {'suit': 'spades', 'value': 2}], 
             [{'suit': 'hearts', 'value': 9}, {'suit': 'diamonds', 'value': 1}, {'suit': 'clubs', 'value': 7}, {'suit': 'spades', 'value': 4}],
             [{'suit': 'hearts', 'value': 5}, {'suit': 'diamonds', 'value': 3}, {'suit': 'clubs', 'value': 8}, {'suit': 'spades', 'value': 2}],
             [{'suit': 'hearts', 'value': 9}, {'suit': 'diamonds', 'value': 1}, {'suit': 'clubs', 'value': 7}, {'suit': 'spades', 'value': 4}],
             [{'suit': 'hearts', 'value': 5}, {'suit': 'diamonds', 'value': 3}, {'suit': 'clubs', 'value': 8}, {'suit': 'spades', 'value': 2}]]
    assert generateResultTree(cards) == [0, 0, 0, 0, 0]

def test_generateResultTree_5():
    cards = [[{'suit': 'hearts', 'value': 5}, {'suit': 'diamonds', 'value': 3}, {'suit': 'clubs', 'value': 8}, {'suit': 'spades', 'value': 2}], 
             [{'suit': 'hearts', 'value': 9}, {'suit': 'diamonds', 'value': 1}, {'suit': 'clubs', 'value': 7}, {'suit': 'spades', 'value': 4}],
             [{'suit': 'hearts', 'value': 5}, {'suit': 'diamonds', 'value': 3}, {'suit': 'clubs', 'value': 8}, {'suit': '
