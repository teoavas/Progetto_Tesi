from funzione import identify_distance_type

def test_identify_distance_type_1():
    assert identify_distance_type("hello", "world") == ("trans", "", "", "", "")

def test_identify_distance_type_2():
    assert identify_distance_type("", "") == ("None", "", "", "", "")

def test_identify_distance_type_3():
    assert identify_distance_type("a", "b") == ("sub", "a", "b", "", "")

def test_identify_distance_type_4():
    assert identify_distance_type("ab", "c") == ("trans", "ac", "", "", "")

def test_identify_distance_type_5():
    assert identify_distance_type("abc", "") == ("ins", "", "c", "", "")

def test_identify_distance_type_6():
    assert identify_distance_type("", "abc") == ("ins", "a", "", "b", "")

def test_identify_distance_type_7():
    assert identify_distance_type("ab", "cd") == ("trans", "ad", "bc", "", "")
