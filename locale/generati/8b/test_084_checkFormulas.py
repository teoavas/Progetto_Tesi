from funzione import checkFormulas

def test_checkFormulas_1():
    arguments = {'a': 1, 'b': 2}
    formulaTuple = [('a',), ('b', 'c')]
    state = {'a': [1], 'b': [3]}
    assert checkFormulas(arguments, formulaTuple, state) == False

def test_checkFormulas_2():
    arguments = {'a': 1, 'b': 2}
    formulaTuple = [('a',), ('b', 'c')]
    state = {'a': [1], 'b': [3]}
    assert checkFormulas(arguments, formulaTuple, state) == False

def test_checkFormulas_3():
    arguments = {'a': 1, 'b': 2}
    formulaTuple = [('a',), ('b', 'c')]
    state = {'a': [1], 'b': [3]}
    assert checkFormulas(arguments, formulaTuple, state) == False

def test_checkFormulas_4():
    arguments = {'a': 1, 'b': 2}
    formulaTuple = [('a',), ('b', 'c')]
    state = {'a': [1], 'b': [3]}
    assert checkFormulas(arguments, formulaTuple, state) == False

def test_checkFormulas_5():
    arguments = {'a': 1, 'b': 2}
    formulaTuple = [('a',), ('b', 'c')]
    state = {'a': [1], 'b': [3]}
    assert checkFormulas(arguments, formulaTuple, state) == False

def test_checkFormulas_6():
    arguments = {'a': 1, 'b': 2}
    formulaTuple = [('a',), ('b', 'c')]
    state = {'a': [1], 'b': [3]}
    assert checkFormulas(arguments, formulaTuple, state) == False

def test_checkFormulas_7():
    arguments = {'a': 1, 'b': 2}
    formulaTuple = [('a',), ('b', 'c')]
    state = {'a': [1], 'b': [3]}
    assert checkFormulas(arguments, formulaTuple, state) == False

def test_checkFormulas_8():
    arguments = {'a': 1, 'b': 2}
    formulaTuple = [('a',), ('b', 'c')]
    state = {'a': [1], 'b': [3]}
    assert checkFormulas(arguments, formulaTuple, state) == False
