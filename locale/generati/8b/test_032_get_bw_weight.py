from funzione import get_bw_weight

def test_get_bw_weight_1():
    flags = [Flag.GUARD, Flag.EXIT]
    position = 'g'
    bw_weights = {'Wgd': 10.0, 'Wgg': 20.0, 'Wgm': 30.0}
    assert get_bw_weight(flags, position, bw_weights) == 10.0

def test_get_bw_weight_2():
    flags = [Flag.GUARD]
    position = 'g'
    bw_weights = {'Wgd': 10.0, 'Wgg': 20.0, 'Wgm': 30.0}
    assert get_bw_weight(flags, position, bw_weights) == 20.0

def test_get_bw_weight_3():
    flags = []
    position = 'g'
    bw_weights = {'Wgd': 10.0, 'Wgg': 20.0, 'Wgm': 30.0}
    assert get_bw_weight(flags, position, bw_weights) == 30.0

def test_get_bw_weight_4():
    flags = [Flag.GUARD]
    position = 'm'
    bw_weights = {'Wmd': 10.0, 'Wmg': 20.0, 'Wmm': 30.0}
    assert get_bw_weight(flags, position, bw_weights) == 20.0

def test_get_bw_weight_5():
    flags = [Flag.EXIT]
    position = 'm'
    bw_weights = {'Wmd': 10.0, 'Wmg': 20.0, 'Wmm': 30.0}
    assert get_bw_weight(flags, position, bw_weights) == 30.0

def test_get_bw_weight_6():
    flags = [Flag.GUARD]
    position = 'e'
    bw_weights = {'Wed': 10.0, 'Weg': 20.0, 'Wee': 30.0}
    assert get_bw_weight(flags, position, bw_weights) == 20.0

def test_get_bw_weight_7():
    flags = [Flag.EXIT]
    position = 'e'
    bw_weights = {'Wed': 10.0, 'Weg': 20.0, 'Wee': 30.0}
    assert get_bw_weight(flags, position, bw_weights) == 30.0

def test_get_bw_weight_8():
    flags = [Flag.HSDIR]
    position = 'h2'
    bw_weights = {}
    assert get_bw_weight(flags, position, bw_weights) == 1.0
