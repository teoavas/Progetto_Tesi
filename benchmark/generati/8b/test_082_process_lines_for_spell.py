from funzione import process_lines_for_spell

def test_process_lines_for_spell_1():
    lines = [(10, 20, False), (30, 40, True)]
    dh = 5
    result = process_lines_for_spell(lines, dh)
    assert len(result) == 8

def test_process_lines_for_spell_2():
    lines = [(10, 20, False), (30, 40, False)]
    dh = 5
    result = process_lines_for_spell(lines, dh)
    assert result[0] == 2
    assert result[1] == 2
    assert result[2] == 0
    assert result[3] == 0

def test_process_lines_for_spell_3():
    lines = [(10, 20, False), (30, 40, True)]
    dh = 5
    result = process_lines_for_spell(lines, dh)
    assert result[4] == 10 + 30
    assert result[5] == 20 + 40
    assert result[6] == 10 / 1.5
    assert result[7] == 20 - (30 - 10 / 1.5)

def test_process_lines_for_spell_4():
    lines = [(10, 20, False), (30, 40, True)]
    dh = 5
    base_heal = 20
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result[0] == 2
    assert result[1] == 2
    assert result[2] == 0
    assert result[3] == 0

def test_process_lines_for_spell_5():
    lines = [(10, 20, False), (30, 40, True)]
    dh = 5
    base_heal = 10
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result[0] == 1
    assert result[1] == 1
    assert result[2] == 0
    assert result[3] == 0

def test_process_lines_for_spell_6():
    lines = [(10, 20, False), (30, 40, True)]
    dh = 5
    base_heal = 30
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result[0] == 0
    assert result[1] == 0
    assert result[2] == 0
    assert result[3] == 0

def test_process_lines_for_spell_7():
    lines = [(10, 20, False), (30, 40, True)]
    dh = 5
    base_heal = 10
    result = process_lines_for_spell(lines, dh, base_heal)
    assert result[4] == 10
    assert result[5] == 20
    assert result[6] == 10
    assert result[7] == 20 - (30 - 10)
