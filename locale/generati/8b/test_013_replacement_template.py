from funzione import replacement_template

def test_replacement_template_1():
    assert replacement_template('Hello $&', 'Hello world', (0, 5), ['world']) == 'Hello world'

def test_replacement_template_2():
    assert replacement_template('Hello $`', 'Hello world', (0, 5), []) == 'Hello '

def test_replacement_template_3():
    assert replacement_template('Hello $\'', 'Hello world', (0, 5), ['world']) == 'Hello world'

def test_replacement_template_4():
    assert replacement_template('Hello $1', 'Hello world', (0, 5), ['world']) == 'Hello world'

def test_replacement_template_5():
    assert replacement_template('Hello $10', 'Hello world', (0, 5), ['world']) == 'Hello world'

def test_replacement_template_6():
    assert replacement_template('Hello $a', 'Hello world', (0, 5), ['world']) == 'Hello $a'

def test_replacement_template_7():
    assert replacement_template('Hello $1$2', 'Hello world', (0, 5), ['world', 'test']) == 'Hello worldtest'
