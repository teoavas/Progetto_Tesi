from funzione import uoc_railfence_encrypt

def test_uoc_railfence_encrypt_1():
    assert uoc_railfence_encrypt('hello', [3, []]) == 'hloel'

def test_uoc_railfence_encrypt_2():
    assert uoc_railfence_encrypt('hello', [3, [(0, 0), (2, 0)]]) == 'hloel'

def test_uoc_railfence_encrypt_3():
    assert uoc_railfence_encrypt('hello', [3, [(0, 0), (2, 0), (1, 1)]]) == 'hloe'

def test_uoc_railfence_encrypt_4():
    assert uoc_railfence_encrypt('hello', [3, [(0, 0), (2, 0), (1, 1), (0, 2)]]) == 'hloe'

def test_uoc_railfence_encrypt_5():
    assert uoc_railfence_encrypt('hello', [3, [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2)]]) == 'hloe'

def test_uoc_railfence_encrypt_6():
    assert uoc_railfence_encrypt('hello', [3, [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2), (1, 3)]]) == 'hloe'

def test_uoc_railfence_encrypt_7():
    assert uoc_railfence_encrypt('hello', [3, [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2), (1, 3), (0, 4)]]) == 'hloe'
