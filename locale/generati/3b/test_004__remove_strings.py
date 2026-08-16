from funzione import _remove_strings

def test__remove_strings_1():
    assert _remove_strings("Hello 'world'") == "Hello world"

def test__remove_strings_2():
    assert _remove_strings("Hello \"world\"") == "Hello world"

def test__remove_strings_3():
    assert _remove_strings("Hello 'world' and \"foo bar\"") == "Hello world and foo bar"

def test__remove_strings_4():
    assert _remove_strings("Hello 'world' with \\backslash") == "Hello world with \\\b"

def test__remove_strings_5():
    assert _remove_strings("Hello \"world\" with \\backslash") == "Hello world with \\\b"

def test__remove_strings_6():
    assert _remove_strings("Hello 'world' and \"foo bar\" with \\backslash") == "Hello world and foo bar with \\\b"

def test__remove_strings_7():
    assert _remove_strings("Hello 'world' with \\backslash and \"foo bar\"") == "Hello world with \\\b and foo bar"
