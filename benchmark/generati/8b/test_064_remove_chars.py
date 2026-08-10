from funzione import remove_chars

def test_remove_chars_1():
    assert remove_chars('Hello World', ' \t') == 'HelloWorld'

def test_remove_chars_2():
    assert remove_chars('Hello World', ' \t', 'Hello') == 'World'

def test_remove_chars_3():
    assert remove_chars('Hello World', ' \t', 'Hello', ['World']) == ''

def test_remove_chars_4():
    assert remove_chars('Hello World', ' \t', 'Hello', 'World') == ''

def test_remove_chars_5():
    assert remove_chars('Hello World', ' \t', 'Hello', 'World', quotes='\'"') == ''

def test_remove_chars_6():
    assert remove_chars('Hello World', ' \t', 'Hello', 'World', quotes='\'"') == ''

def test_remove_chars_7():
    assert remove_chars('Hello World', ' \t', 'Hello', 'World', quotes='\'"') == ''

def test_remove_chars_8():
    assert remove_chars('Hello World', ' \t', 'Hello', 'World', quotes='\'"') == ''
