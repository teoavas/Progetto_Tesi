from funzione import identify_distance_type

def test_identify_distance_type_1():
    assert identify_distance_type("kitten", "sitting") == ("sub", "k", "i", "ki", "k")

def test_identify_distance_type_2():
    assert identify_distance_type("kitten", "sittin") == ("sub", "k", "i", "ki", "k")

def test_identify_distance_type_3():
    assert identify_distance_type("kitten", "sit") == ("ins", "", "t", "#t", "#t")

def test_identify_distance_type_4():
    assert identify_distance_type("kitten", "sittin") == ("sub", "k", "i", "ki", "k")

def test_identify_distance_type_5():
    assert identify_distance_type("kitten", "kitten") == ("None", "", "", "", "")

def test_identify_distance_type_6():
    assert identify_distance_type("kitten", "kittens") == ("ins", "s", "", "s", "s")

def test_identify_distance_type_7():
    assert identify_distance_type("kitten", "kit") == ("del", "t", "", "", "")

def test_identify_distance_type_8():
    assert identify_distance_type("kitten", "sittin") == ("sub", "k", "i", "ki", "k")
