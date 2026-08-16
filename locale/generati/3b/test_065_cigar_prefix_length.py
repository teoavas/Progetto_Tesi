from funzione import cigar_prefix_length

def test_cigar_prefix_length_1():
    assert cigar_prefix_length('M10', 100) == (10, 10)

def test_cigar_prefix_length_2():
    assert cigar_prefix_length('X20', 50) == (50, 30)

def test_cigar_prefix_length_3():
    assert cigar_prefix_length('=', 200) == (200, 200)

def test_cigar_prefix_length_4():
    with pytest.raises(AssertionError):
        cigar_prefix_length('D100', 150)

def test_cigar_prefix_length_5():
    assert cigar_prefix_length('I50', 100) == (0, 50)

def test_cigar_prefix_length_6():
    assert cigar_prefix_length('M10X20', 100) == (30, 50)

def test_cigar_prefix_length_7():
    with pytest.raises(AssertionError):
        cigar_prefix_length('N100', 150)
