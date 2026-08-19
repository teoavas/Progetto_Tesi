from funzione import diffsents

def test_diffsents_1():
    sa = "hello"
    sb = "world"
    expected_output = (0, 4, 0, 5)
    assert diffsents(sa, sb) == expected_output

def test_diffsents_2():
    sa = "abcdefg"
    sb = "abcdehgf"
    expected_output = (1, 6, 1, 7)
    assert diffsents(sa, sb) == expected_output

def test_diffsents_3():
    sa = "abcdefgh"
    sb = "abcd"
    expected_output = (0, 4, 0, 4)
    assert diffsents(sa, sb) == expected_output

def test_diffsents_4():
    sa = ""
    sb = "hello"
    expected_output = (-1, -1, 0, 5)
    assert diffsents(sa, sb) == expected_output

def test_diffsents_5():
    sa = "hello"
    sb = ""
    expected_output = (0, 4, -1, -1)
    assert diffsents(sa, sb) == expected_output

def test_diffsents_6():
    sa = "abcdefg"
    sb = "abcdehgf"
    expected_output = (1, 6, 1, 7)
    assert diffsents(sa, sb) == expected_output
