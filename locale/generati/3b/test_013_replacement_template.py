from funzione import replacement_template

def test_replacement_template_1():
    assert replacement_template('$', 'hello world', (0, 5), [1, 2]) == '$12'

def test_replacement_template_2():
    assert replacement_template('&', 'hello world', (0, 5), ['a', 'b']) == 'ab'

def test_replacement_template_3():
    assert replacement_template('`', 'hello world', (0, 5), ['a', 'b']) == 'helo'

def test_replacement_template_4():
    assert replacement_template('\'', 'hello world', (0, 5), ['a', 'b']) == 'world'

def test_replacement_template_5():
    assert replacement_template('$123', 'hello world', (0, 5), [1, 2]) == '$123'

def test_replacement_template_6():
    assert replacement_template('abc$123', 'hello world', (0, 5), ['a', 'b']) == 'ab12'

def test_replacement_template_7():
    assert replacement_template('$', '', (0, 5), [1, 2]) == '$'
