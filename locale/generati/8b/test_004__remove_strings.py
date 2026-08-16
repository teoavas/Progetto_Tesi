from funzione import _remove_strings

def test__remove_strings_1():
    assert _remove_strings("Hello 'world'!") == "Helloworld!"

def test__remove_strings_2():
    assert _remove_strings('This is a "string"') == "This is a string"

def test__remove_strings_3():
    assert _remove_strings('"This is another "string""') == "This is another string"

def test__remove_strings_4():
    assert _remove_strings("No strings here") == "No strings here"

def test__remove_strings_5():
    assert _remove_strings("'Single quote' and \"double quote\"") == "'Single quote' and double quote"

def test__remove_strings_6():
    assert _remove_strings('No strings') == 'No strings'

def test__remove_strings_7():
    assert _remove_strings('"String" with "more" strings') == '"String" with more strings'
