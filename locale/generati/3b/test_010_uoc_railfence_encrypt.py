from funzione import uoc_railfence_encrypt

def test_uoc_railfence_encrypt_1():
    message = 'Hello'
    key = (3, 2)
    ciphertext = uoc_railfence_encrypt(message, key)
    assert len(ciphertext) == len(message)

def test_uoc_railfence_encrypt_2():
    message = 'World'
    key = (4, 1)
    ciphertext = uoc_railfence_encrypt(message, key)
    assert any(char in ciphertext for char in message)

def test_uoc_railfence_encrypt_3():
    message = ''
    key = (5, 0)
    ciphertext = uoc_railfence_encrypt(message, key)
    assert len(ciphertext) == 0

def test_uoc_railfence_encrypt_4():
    message = 'Python'
    key = (2, 1)
    ciphertext = uoc_railfence_encrypt(message, key)
    assert any(char in ciphertext for char in message)

def test_uoc_railfence_encrypt_5():
    message = 'Programming'
    key = (3, 2)
    ciphertext = uoc_railfence_encrypt(message, key)
    assert len(ciphertext) == len(message)

def test_uoc_railfence_encrypt_6():
    message = 'Test'
    key = (1, 0)
    ciphertext = uoc_railfence_encrypt(message, key)
    assert any(char in ciphertext for char in message)

def test_uoc_railfence_encrypt_7():
    message = 'Encryption'
    key = (4, 3)
    ciphertext = uoc_railfence_encrypt(message, key)
    assert len(ciphertext) == len(message)
