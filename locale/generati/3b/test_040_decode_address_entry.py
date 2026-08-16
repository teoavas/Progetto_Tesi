from funzione import decode_address_entry

def test_decode_address_entry_1():
    assert decode_address_entry("0x1234:1,2,3", False) == [[0x1234], [1, 2, 3]]

def test_decode_address_entry_2():
    assert decode_address_entry("0x1234:1,2,3", True) == [[0x1234, 1, 2, 3]]

def test_decode_address_entry_3():
    assert decode_address_entry("0x1234:1,2,3", False) == [[0x1234], [1, 2, 3]]

def test_decode_address_entry_4():
    assert decode_address_entry("0x1234:1,2,3", True) == [[0x1234, 1, 2, 3]]

def test_decode_address_entry_5():
    assert decode_address_entry("0x1234:1,2,3", False) == [[0x1234], [1, 2, 3]]

def test_decode_address_entry_6():
    assert decode_address_entry("0x1234:1,2,3", True) == [[0x1234, 1, 2, 3]]

def test_decode_address_entry_7():
    assert decode_address_entry("0x1234:1,2,3", False) == [[0x1234], [1, 2, 3]]

def test_decode_address_entry_8():
    assert decode_address_entry("0x1234:1,2,3", True) == [[0x1234, 1, 2, 3]]
