from funzione import lumen_type

def test_lumen_type_1():
    assert len(lumen_type([['0', '0'], ['1', '2']], {'0'})) == 2

def test_lumen_type_2():
    assert lumen_type([['0', '0'], ['1', '2']], {'0'}, ['1']) == {0: 'mutantsmi'}

def test_lumen_type_3():
    assert len(lumen_type([['0', '0'], ['1', '2']], {'0'}, [], [], [])) == 2

def test_lumen_type_4():
    assert lumen_type([['0', '0'], ['1', '2']], {'0'}, ['1']) == {0: 'TEmi'}

def test_lumen_type_5():
    assert len(lumen_type([['0', '0'], ['1', '2']], {'0'}, [], ['1'])) == 2

def test_lumen_type_6():
    assert lumen_type([['0', '0'], ['1', '2']], {'0'}, ['1'], []) == {0: 'mutantsmi'}

def test_lumen_type_7():
    assert len(lumen_type([['0', '0'], ['1', '2']], {'0'}, [], [], ['1'])) == 2
