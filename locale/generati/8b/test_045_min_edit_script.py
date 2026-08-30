from funzione import min_edit_script

def test_min_edit_script_1():
    assert min_edit_script("", "") == ""

def test_min_edit_script_2():
    assert min_edit_script("a", "") == ""

def test_min_edit_script_3():
    assert min_edit_script("", "a") == ""

def test_min_edit_script_4():
    assert min_edit_script("a", "a") == "→"

def test_min_edit_script_5():
    assert min_edit_script("abc", "abc") == "→→"

def test_min_edit_script_6():
    assert min_edit_script("abc", "def") == "a+d-e+c"

def test_min_edit_script_7():
    assert min_edit_script("abcdef", "abc") == "a+d-e+f"

def test_min_edit_script_8():
    assert min_edit_script("abc", "abcdef") == "a+d-e+f"
