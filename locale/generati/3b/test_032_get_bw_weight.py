from funzione import get_bw_weight

def test_get_bw_weight_1():
    flags = [Flag.GUARD, Flag.EXIT]
    position = 'g'
    bw_weights = {'Wgd': 10, 'Wgg': 20}
    assert get_bw_weight(flags, position, bw_weights) == bw_weights['Wgd']

def test_get_bw_weight_2():
    flags = [Flag.GUARD]
    position = 'g'
    bw_weights = {'Wgg': 20}
    assert get_bw_weight(flags, position, bw_weights) == bw_weights['Wgg']

def test_get_bw_weight_3():
    flags = [Flag.EXIT]
    position = 'g'
    bw_weights = {'Wgm': 30}
    assert get_bw_weight(flags, position, bw_weights) == bw_weights['Wgm']

def test_get_bw_weight_4():
    flags = []
    position = 'g'
    bw_weights = {'Wgd': 10, 'Wgg': 20}
    assert get_bw_weight(flags, position, bw_weights) == 0

def test_get_bw_weight_5():
    flags = [Flag.STABLE]
    position = 'i'
    bw_weights = {'Wmm': 40}
    assert get_bw_weight(flags, position, bw_weights) == bw_weights['Wmm']

def test_get_bw_weight_6():
    flags = [Flag.GUARD, Flag.EXIT]
    position = 'm'
    bw_weights = {'Wmd': 50}
    assert get_bw_weight(flags, position, bw_weights) == bw_weights['Wmd']

def test_get_bw_weight_7():
    flags = [Flag.GUARD]
    position = 'i'
    bw_weights = {'Wmg': 60}
    assert get_bw_weight(flags, position, bw_weights) == bw_weights['Wmg']
