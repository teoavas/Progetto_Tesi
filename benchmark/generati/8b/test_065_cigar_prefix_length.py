from funzione import cigar_prefix_length

def test_cigar_prefix_length_1():
    assert cigar_prefix_length("10M", 10) == (10, 10)

def test_cigar_prefix_length_2():
    assert cigar_prefix_length("5M10D", 15) == (15, 5)

def test_cigar_prefix_length_3():
    assert cigar_prefix_length("5M10I", 15) == (15, 15)

def test_cigar_prefix_length_4():
    assert cigar_prefix_length("5M10S", 15) == (15, 15)

def test_cigar_prefix_length_5():
    assert cigar_prefix_length("5M10H", 15) == (15, 15)

def test_cigar_prefix_length_6():
    assert cigar_prefix_length("5M10=", 15) == (15, 25)

def test_cigar_prefix_length_7():
    assert cigar_prefix_length("5M10X", 15) == (15, 25)

def test_cigar_prefix_length_8():
    assert cigar_prefix_length("5M10N", 15) == (15, 15)  # N operator should be handled as M
