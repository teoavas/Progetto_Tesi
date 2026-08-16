import pytest

def test_decode_address_entry_1():
    assert decode_address_entry("0x1234:2,3", sort=True) == [[1], [2], [3]]

def test_decode_address_entry_2():
    assert decode_address_entry("0x5678:1,2", sort=False) == [[1], [2], [0]]

def test_decode_address_entry_3():
    assert decode_address_entry("0x9012:4,5", sort=True) == [[0], [1], [2], [3]]

def test_decode_address_entry_4():
    assert decode_address_entry("0x1111:1,2,3", sort=False) == [[1], [2], [0], [1], [2], [0]]

def test_decode_address_entry_5():
    assert decode_address_entry("0x2222:2,3", sort=True) == [[2], [3], [0]]

def test_decode_address_entry_6():
    assert decode_address_entry("0x3333:4,5", sort=False) == [[4], [5], [0], [1], [2], [3]]

def test_decode_address_entry_7():
    assert decode_address_entry("0x4444:1,2,3", sort=True) == [[1], [2], [0], [1], [2], [0]]

def test_decode_address_entry_8():
    assert decode_address_entry("0x5555:2,3", sort=False) == [[2], [3], [0], [1], [2], [0]]
