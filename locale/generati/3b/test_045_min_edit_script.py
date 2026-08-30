from funzione import min_edit_script

def test_min_edit_script_1():
    assert min_edit_script("kitten", "sitting") == "kitten→sitting"

def test_min_edit_script_2():
    assert min_edit_script("abc", "def") == "abc-d+def"

def test_min_edit_script_3():
    assert min_edit_script("", "hello") == "hello+"

def test_min_edit_script_4():
    assert min_edit_script("hello", "") == ""

def test_min_edit_script_5():
    assert min_edit_script("abc", "") == "abc-"

def test_min_edit_script_6():
    assert min_edit_script("abc", "abc") == ""

def test_min_edit_script_7():
    assert min_edit_script("abc", "abcd") == "abc-d+abcd"

def test_min_edit_script_8():
    assert min_edit_script("abcdef", "zbcdfg") == "abcdef→zbcdfg"
