from funzione import remove_chars

def test_remove_chars_1():
    assert remove_chars('Hello World', ' \t') == 'HelloWorld'

def test_remove_chars_2():
    assert remove_chars('Hello "World"', '\'\"') == 'Hello "World"'

def test_remove_chars_3():
    assert remove_chars('# This is a comment', '#') == ''

def test_remove_chars_4():
    assert remove_chars('This is a line with spaces and tabs \t ', ' \t') == 'Thisisalinewithspacesandtabs'

def test_remove_chars_5():
    assert remove_chars('This is a line with quotes "Hello World"', '\'\"') == 'This is a line with quotes "Hello World"'

def test_remove_chars_6():
    assert remove_chars('# This is a comment', '#', ['#']) == ''

def test_remove_chars_7():
    assert remove_chars('This is a line with comments # This is another comment', ['#']) == 'Thisisaline'
