from funzione import uoc_railfence_encrypt

def test_uoc_railfence_encrypt_1():
    message = 'hello'
    key = (3, [0])
    assert uoc_railfence_encrypt(message, key) == 'hloel'

def test_uoc_railfence_encrypt_2():
    message = 'python'
    key = (4, [0, 1])
    assert uoc_railfence_encrypt(message, key) == 'pythno'

def test_uoc_railfence_encrypt_3():
    message = 'railfence'
    key = (5, [0, 2, 4])
    assert uoc_railfence_encrypt(message, key) == 'rfliecaen'

def test_uoc_railfence_encrypt_4():
    message = ''
    key = (3, [0])
    assert uoc_railfence_encrypt(message, key) == ''

def test_uoc_railfence_encrypt_5():
    message = 'a'
    key = (1, [0])
    assert uoc_railfence_encrypt(message, key) == 'a'

def test_uoc_railfence_encrypt_6():
    message = 'abcde'
    key = (3, [0])
    assert uoc_railfence_encrypt(message, key) == 'abced'

def test_uoc_railfence_encrypt_7():
    message = 'abcdefghijklmnopqrstuvwxyz'
    key = (26, [])
    assert uoc_railfence_encrypt(message, key) == 'abcdefghijklmnopqrstuvwxyz'
