from funzione import process_lines_for_spell

def test_process_lines_for_spell_1():
    lines = [(10.0, 20.0, False), (15.0, 30.0, True)]
    dh = 5.0
    base_heal = None
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result == (2, 1, 1, 1, 20.0, 10.0, 15.0, 25.0)

def test_process_lines_for_spell_2():
    lines = [(5.0, 10.0, False), (7.0, 12.0, True)]
    dh = 3.0
    base_heal = None
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result == (2, 1, 1, 1, 10.5, 6.0, 7.5, 9.0)

def test_process_lines_for_spell_3():
    lines = [(20.0, 30.0, False), (25.0, 35.0, True)]
    dh = 10.0
    base_heal = None
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result == (2, 1, 1, 1, 30.0, 20.0, 25.0, 35.0)

def test_process_lines_for_spell_4():
    lines = [(10.0, 20.0, False), (15.0, 30.0, True)]
    dh = 5.0
    base_heal = 12.0
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result == (2, 1, 1, 1, 20.0, 10.0, 15.0, 25.0)

def test_process_lines_for_spell_5():
    lines = [(5.0, 10.0, False), (7.0, 12.0, True)]
    dh = 3.0
    base_heal = None
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result == (2, 1, 1, 1, 10.5, 6.0, 7.5, 9.0)

def test_process_lines_for_spell_6():
    lines = [(20.0, 30.0, False), (25.0, 35.0, True)]
    dh = 10.0
    base_heal = None
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result == (2, 1, 1, 1, 30.0, 20.0, 25.0, 35.0)

def test_process_lines_for_spell_7():
    lines = [(10.0, 20.0, False), (15.0, 30.0, True)]
    dh = 5.0
    base_heal = None
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result == (2, 1, 1, 1, 20.0, 10.0, 15.0, 25.0)

def test_process_lines_for_spell_8():
    lines = [(5.0, 10.0, False), (7.0, 12.0, True)]
    dh = 3.0
    base_heal = None
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result == (2, 1, 1, 1, 10.5, 6.0, 7.5, 9.0)
