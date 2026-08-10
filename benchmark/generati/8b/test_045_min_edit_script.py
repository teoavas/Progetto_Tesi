from funzione import min_edit_script

def test_min_edit_script_1():
    source = "kitten"
    target = "sitting"
    assert min_edit_script(source, target) == "k-s+t-i-n-g"

def test_min_edit_script_2():
    source = "abc"
    target = "abc"
    assert min_edit_script(source, target) == ""

def test_min_edit_script_3():
    source = "abc"
    target = "abcd"
    assert min_edit_script(source, target) == "c+"

def test_min_edit_script_4():
    source = "abcd"
    target = "abc"
    assert min_edit_script(source, target) == "d-"

def test_min_edit_script_5():
    source = "abc"
    target = "def"
    assert min_edit_script(source, target) == "a-b-c+d-e-f"

def test_min_edit_script_6():
    source = ""
    target = "abc"
    assert min_edit_script(source, target) == "a+b+c"

def test_min_edit_script_7():
    source = "abc"
    target = ""
    assert min_edit_script(source, target) == "a-b-c"

def test_min_edit_script_8():
    source = "abc"
    target = "abc"
    allow_copy = True
    assert min_edit_script(source, target, allow_copy) == ""
