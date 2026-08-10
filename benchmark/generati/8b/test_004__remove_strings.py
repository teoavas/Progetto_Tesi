from funzione import _remove_strings

def test__remove_strings_1():
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World' \"Python\"") == "Hello World Python"
    assert _remove_strings('Hello "World" \'Python\'') == 'Hello World Python'

def test__remove_strings_2():
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'

def test__remove_strings_3():
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World' \"Python\"") == "Hello World Python"
    assert _remove_strings('Hello "World" \'Python\'') == 'Hello World Python'

def test__remove_strings_4():
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'

def test__remove_strings_5():
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World'") == "Hello World"

def test__remove_strings_6():
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'

def test__remove_strings_7():
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World'") == "Hello World"

def test__remove_strings_8():
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
    assert _remove_strings("Hello 'World'") == "Hello World"
    assert _remove_strings('Hello "World"') == 'Hello World'
