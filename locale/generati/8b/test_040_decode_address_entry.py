from funzione import decode_address_entry

def test_decode_address_entry_1():
    result = decode_address_entry("0x1234:2,3")
    expected_result = [["0x1234", 2, 3], ["0x1234", 2, 0], ["0x1234", 0, 3]]
    assert result == expected_result

def test_decode_address_entry_2():
    result = decode_address_entry("0x1234:2,3:1")
    expected_result = [["0x1234", 2, 3], ["0x1234", 2, 0], ["0x1234", 0, 3]]
    assert result == expected_result

def test_decode_address_entry_3():
    result = decode_address_entry("0x1234:2,3:1,2")
    expected_result = [["0x1234", 2, 3], ["0x1234", 2, 0], ["0x1234", 0, 3]]
    assert result == expected_result

def test_decode_address_entry_4():
    result = decode_address_entry("0x1234:2,3:1,2:3")
    expected_result = [["0x1234", 2, 3], ["0x1234", 2, 0], ["0x1234", 0, 3]]
    assert result == expected_result

def test_decode_address_entry_5():
    result = decode_address_entry("0x1234:2,3:1,2:3:4")
    expected_result = [["0x1234", 2, 3], ["0x1234", 2, 0], ["0x1234", 0, 3]]
    assert result == expected_result

def test_decode_address_entry_6():
    result = decode_address_entry("0x1234:2,3:1,2:3:4:5")
    expected_result = [["0x1234", 2, 3], ["0x1234", 2, 0], ["0x1234", 0, 3]]
    assert result == expected_result

def test_decode_address_entry_7():
    result = decode_address_entry("0x1234:2,3")
    expected_result = [["0x1234", 2, 3], ["0x1234", 2, 0], ["0x1234", 0, 3]]
    assert result == expected_result

def test_decode_address_entry_8():
    result = decode_address_entry("0x1234:2,3", sort=True)
    expected_result = [["0x1234", 0, 3], ["0x1234", 2, 3], ["0x1234", 2, 0]]
    assert result == expected_result
