from funzione import identify_distance_type

def test_identify_distance_type_1():
    assert identify_distance_type("kitten", "sitting") == ("sub", 't', 'i', 'it', 'ti')

def test_identify_distance_type_2():
    assert identify_distance_type("", "") == ("None", '', '', '', '')

def test_identify_distance_type_3():
    assert identify_distance_type("abcde", "abcde") == ("None", '', '', '', '')

def test_identify_distance_type_4():
    assert identify_distance_type("kitten", "sittin") == ("del", 't', '', 'it', 'ti')

def test_identify_distance_type_5():
    assert identify_distance_type("sitting", "kitten") == ("ins", '', 'i', 'ki', 'kt')

def test_identify_distance_type_6():
    assert identify_distance_type("abcde", "abcd") == ("sub", 'e', 'd', 'de', 'ab')

def test_identify_distance_type_7():
    assert identify_distance_type("abcde", "abcdef") == ("ins", '', 'f', 'f', 'bc')

def test_identify_distance_type_8():
    assert identify_distance_type("abcde", "dcbae") == ("trans", 'ab', 'c', 'cd', 'ae')
