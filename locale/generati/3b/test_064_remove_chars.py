from funzione import remove_chars

def test_remove_chars_1():
    assert remove_chars('Hello, World!', ' ', ',') == 'HelloWorld!'

def test_remove_chars_2():
    assert remove_chars('This is a comment', ' ', '#') == 'Thisisacomment'

def test_remove_chars_3():
    assert remove_chars('This is "a quoted string"', '"', '') == 'Thisisaquotedstring'

def test_remove_chars_4():
    assert remove_chars('This is a line with tabs and spaces', '\t', ' ') == 'Thisisanlinespaces'

def test_remove_chars_5():
    assert remove_chars('This is a line with comments', '#') == 'Thisisalinewithcomments'

def test_remove_chars_6():
    assert remove_chars('', ' ', '') == ''

def test_remove_chars_7():
    assert remove_chars('This is a line with multiple quotes', '"', '"') == 'Thisisalinenwithmultiplequotes'
