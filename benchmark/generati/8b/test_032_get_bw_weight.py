from funzione import get_bw_weight

def test_get_bw_weight_1():
    flags = ['guard', 'exit']
    position = 'g'
    bw_weights = {'Wgd': 1.0, 'Wgg': 2.0, 'Wgm': 3.0, 'Wge': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 1.0

def test_get_bw_weight_2():
    flags = ['guard']
    position = 'g'
    bw_weights = {'Wgd': 1.0, 'Wgg': 2.0, 'Wgm': 3.0, 'Wge': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 2.0

def test_get_bw_weight_3():
    flags = ['guard', 'exit']
    position = 'm'
    bw_weights = {'Wmd': 1.0, 'Wmg': 2.0, 'Wmm': 3.0, 'Wme': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 1.0

def test_get_bw_weight_4():
    flags = ['guard']
    position = 'm'
    bw_weights = {'Wmd': 1.0, 'Wmg': 2.0, 'Wmm': 3.0, 'Wme': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 2.0

def test_get_bw_weight_5():
    flags = ['exit']
    position = 'm'
    bw_weights = {'Wmd': 1.0, 'Wmg': 2.0, 'Wmm': 3.0, 'Wme': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 4.0

def test_get_bw_weight_6():
    flags = ['guard', 'exit']
    position = 'e'
    bw_weights = {'Wed': 1.0, 'Weg': 2.0, 'Wee': 3.0, 'Wem': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 1.0

def test_get_bw_weight_7():
    flags = ['guard']
    position = 'e'
    bw_weights = {'Wed': 1.0, 'Weg': 2.0, 'Wee': 3.0, 'Wem': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 2.0

def test_get_bw_weight_8():
    flags = ['exit']
    position = 'e'
    bw_weights = {'Wed': 1.0, 'Weg': 2.0, 'Wee': 3.0, 'Wem': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 3.0

def test_get_bw_weight_9():
    flags = ['guard', 'exit']
    position = 'h2'
    bw_weights = {'Wgd': 1.0, 'Wgg': 2.0, 'Wgm': 3.0, 'Wge': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 1.0

def test_get_bw_weight_10():
    flags = ['guard', 'exit']
    position = 'h3'
    bw_weights = {'Wgd': 1.0, 'Wgg': 2.0, 'Wgm': 3.0, 'Wge': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 0.0

def test_get_bw_weight_11():
    flags = ['guard', 'exit']
    position = 'h3'
    bw_weights = {'Wgd': 1.0, 'Wgg': 2.0, 'Wgm': 3.0, 'Wge': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 0.0

def test_get_bw_weight_12():
    flags = ['guard', 'exit']
    position = 'h2'
    bw_weights = {'Wgd': 1.0, 'Wgg': 2.0, 'Wgm': 3.0, 'Wge': 4.0}
    assert get_bw_weight(flags, position, bw_weights) == 1.0

def test_get_bw_weight_13():
    flags = ['guard', 'exit']
    position = 'h2'
    bw_weights = {'Wgd': 1.0, 'Wgg': 2.0, 'Wgm': 3.0,
