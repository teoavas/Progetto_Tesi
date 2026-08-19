from funzione import cigar_prefix_length

def test_cigar_prefix_length_1():
    result = cigar_prefix_length("10M", 10)
    assert result == (10, 10)

def test_cigar_prefix_length_2():
    result = cigar_prefix_length("5M7I3D", 8)
    assert result == (8, 11)

def test_cigar_prefix_length_3():
    result = cigar_prefix_length("10M20N30S", 15)
    assert result == (15, 25)

def test_cigar_prefix_length_4():
    result = cigar_prefix_length("", 5)
    assert result == (0, 0)

def test_cigar_prefix_length_5():
    result = cigar_prefix_length("10M20I30D", 12)
    assert result == (12, 32)

def test_cigar_prefix_length_6():
    result = cigar_prefix_length("10M20S30N", 15)
    assert result == (15, 25)

def test_cigar_prefix_length_7():
    result = cigar_prefix_length("10M20I30D40M50I60D70M80I90D100M110I120D130M140I150D160M170I180D190M200", 200)
    assert result == (200, 2200)

def test_cigar_prefix_length_8():
    result = cigar_prefix_length("10M20S30N40I50D60M70I80D90M100I110D120M130I140D150M160I170D180M190I200", 200)
    assert result == (200, 2200)
