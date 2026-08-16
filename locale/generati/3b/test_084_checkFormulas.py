from funzione import checkFormulas

def test_checkFormulas_1():
    assert checkFormulas({}, (), 'state') == True

def test_checkFormulas_2():
    state = {'a': 1}
    assert checkFormulas({'b': 2}, ('a',), 'state') == False

def test_checkFormulas_3():
    state = {'a': (1, 2)}
    assert checkFormulas({'b': 2}, ('a', 'c'), 'state') == False

def test_checkFormulas_4():
    state = {'a': (1, 2), 'b': (3, 4)}
    assert checkFormulas({'b': 2}, ('a', 'b'), 'state') == True

def test_checkFormulas_5():
    state = {'a': (1, 2), 'b': (3, 4)}
    assert checkFormulas({'c': 5}, ('a', 'b'), 'state') == False

def test_checkFormulas_6():
    state = {}
    formulaTuple = (('a', 'b'),)
    assert checkFormulas({}, formulaTuple, 'state') == True

def test_checkFormulas_7():
    state = {'a': (1, 2)}
    formulaTuple = (('a',), ('a',))
    assert checkFormulas({'b': 2}, formulaTuple, 'state') == False
