from funzione import replacement_template

def test_replacement_template_1():
    assert replacement_template('Hello $&', 'Hello world', [0, 5], ['world']) == 'Hello world'

def test_replacement_template_2():
    assert replacement_template('Hello $`', 'Hello world', [0, 5], ['world']) == 'Hello '

def test_replacement_template_3():
    assert replacement_template('Hello $\'', 'Hello world', [0, 5], ['world']) == 'Hello world'

def test_replacement_template_4():
    assert replacement_template('Hello $0', 'Hello world', [0, 5], ['world', 'abc']) == 'Hello abc'

def test_replacement_template_5():
    assert replacement_template('Hello $01', 'Hello world', [0, 5], ['world', 'abc']) == 'Hello abc'

def test_replacement_template_6():
    assert replacement_template('Hello $10', 'Hello world', [0, 5], ['world', 'abc']) == 'Hello $10'

def test_replacement_template_7():
    assert replacement_template('Hello $', 'Hello world', [0, 5], ['world', 'abc']) == 'Hello $'

def test_replacement_template_8():
    assert replacement_template('Hello $a', 'Hello world', [0, 5], ['world', 'abc']) == 'Hello $a'
