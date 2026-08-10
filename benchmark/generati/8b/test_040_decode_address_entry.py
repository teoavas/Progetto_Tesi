from funzione import decode_address_entry

def test_decode_address_entry_1():
    assert decode_address_entry("0x1234:1,2:0,1") == [["0x1234", 1, 0], ["0x1234", 1, 1], ["0x1234", 2, 0], ["0x1234", 2, 1]]

def test_decode_address_entry_2():
    assert decode_address_entry("0x1234:1,2:0,1", sort=True) == [["0x1234", 0, 0], ["0x1234", 0, 1], ["0x1234", 1, 0], ["0x1234", 1, 1], ["0x1234", 2, 0], ["0x1234", 2, 1]]

def test_decode_address_entry_3():
    assert decode_address_entry("0x1234:1,2") == [["0x1234", 0, 0], ["0x1234", 0, 1], ["0x1234", 1, 0], ["0x1234", 1, 1], ["0x1234", 2, 0], ["0x1234", 2, 1]]

def test_decode_address_entry_4():
    assert decode_address_entry("0x1234:1,2:0,1,2") == [["0x1234", 1, 0], ["0x1234", 1, 1], ["0x1234", 1, 2], ["0x1234", 2, 0], ["0x1234", 2, 1], ["0x1234", 2, 2]]

def test_decode_address_entry_5():
    assert decode_address_entry("0x1234") == [["0x1234", 0, 0], ["0x1234", 0, 1], ["0x1234", 1, 0], ["0x1234", 1, 1], ["0x1234", 2, 0], ["0x1234", 2, 1]]

def test_decode_address_entry_6():
    assert decode_address_entry("0x1234:1,2:0") == [["0x1234", 1, 0], ["0x1234", 2, 0]]

def test_decode_address_entry_7():
    assert decode_address_entry("0x1234:1,2:0,1", sort=True) == [["0x1234", 0, 0], ["0x1234", 0, 1], ["0x1234", 1, 0], ["0x1234", 1, 1], ["0x1234", 2, 0], ["0x1234", 2, 1]]

def test_decode_address_entry_8():
    assert decode_address_entry("0x1234:1,2:0,1,2,3") == [["0x1234", 1, 0], ["0x1234", 1, 1], ["0x1234", 1, 2], ["0x1234", 2, 0], ["0x1234", 2, 1], ["0x1234", 2, 2]]
