import pytest

def test_uoc_railfence_encrypt_1():
    assert uoc_railfence_encrypt("Hello", [3, 2]) == "H0eLl0"

@pytest.mark.parametrize("message, key, ciphertext", [
    ("Hello World", [3, 2], "H0eLl0W0r1d"),
    ("Python is fun", [5, 4], "P4t4n1s1f1u1n")
])
def test_uoc_railfence_encrypt_2(message, key, ciphertext):
    assert uoc_railfence_encrypt(message, key) == ciphertext

@pytest.mark.parametrize("message, key, ciphertext", [
    ("This is a secret message", [3, 2], "T4i1s1a1s1e1c1s1e1m4se"),
    ("The quick brown fox jumps over the lazy dog", [5, 4])
])
def test_uoc_railfence_encrypt_3(message, key, ciphertext):
    assert uoc_railfence_encrypt(message, key) == ciphertext

@pytest.mark.parametrize("message, key, ciphertext", [
    ("1234567890", [2, 1], "0123456789")
])
def test_uoc_railfence_encrypt_4(message, key, ciphertext):
    assert uoc_railfence_encrypt(message, key) == ciphertext

@pytest.mark.parametrize("message, key, ciphertext", [
    ("abcdefghijklmnopqrstuvwxyz", [3, 2], "abcdefghijklmnopqrstuvwxyz")
])
def test_uoc_railfence_encrypt_5(message, key, ciphertext):
    assert uoc_railfence_encrypt(message, key) == ciphertext

@pytest.mark.parametrize("message, key, ciphertext", [
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", [3, 2], "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
])
def test_uoc_railfence_encrypt_6(message, key, ciphertext):
    assert uoc_railfence_encrypt(message, key) == ciphertext

@pytest.mark.parametrize("message, key, ciphertext", [
    ("1234567890abcdefghijklmnopqrstuvwxyz", [5, 4]),  # upper limit
    ("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ", [3, 2])
])
def test_uoc_railfence_encrypt_7(message, key, ciphertext):
    assert uoc_railfence_encrypt(message, key) == ciphertext

@pytest.mark.parametrize("message, key, ciphertext", [
    ("Hello World", [5, 4]),  # upper limit
    ("Python is fun", [3, 2])
])
def test_uoc_railfence_encrypt_8(message, key, ciphertext):
    assert uoc_railfence_encrypt(message, key) == ciphertext

def test_uoc_railfence_encrypt_empty_message():
    assert uoc_railfence_encrypt("", [3, 2]) == ""

def test_uoc_railfence_encrypt_key_with_zero_length():
    assert uoc_railfence_encrypt("Hello", [0, 1]) == "H0eLl0"

def test_uoc_railfence_encrypt_key_with_one_element():
    assert uoc_railfence_encrypt("Hello", [2]) == "H0eLl0"
