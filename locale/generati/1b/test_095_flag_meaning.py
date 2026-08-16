import pytest

def test_flag_meaning_a0():
    assert flag_meaning('a0') == 'a0 - In attenuator state 0 (None) sometime during flare'

def test_flag_meaning_a1():
    assert flag_meaning('a1') == 'a1 - In attenuator state 1 (Thin) sometime during flare'

def test_flag_meaning_a2():
    assert flag_meaning('a2') == 'a2 - In attenuator state 2 (Thick) sometime during flare'

def test_flag_meaning_a3():
    assert flag_meaning('a3') == 'a3 - In attenuator state 3 (Both) sometime during flare'

def test_flag_meaning_an():
    assert flag_meaning('An') == 'An - Attenuator state (0=None, 1=Thin, 2=Thick, 3=Both) at peak of flare'

def test_flag_meaning_df():
    assert flag_meaning('DF') == 'DF - Front segment counts were decimated sometime during flare'

def test_flag_meaning_dr():
    assert flag_meaning('DR') == 'DR - Rear segment counts were decimated sometime during flare'

def test_flag_meaning_ed():
    assert flag_meaning('ED') == 'ED - Spacecraft eclipse (night) sometime during flare'

def test_flag_meaning_ee():
    assert flag_meaning('EE') == 'EE - Flare ended in spacecraft eclipse (night)'

def test_flag_meaning_es():
    assert flag_meaning('ES') == 'ES - Flare started in spacecraft eclipse (night)'

def test_flag_meaning_fe():
    assert flag_meaning('FE') == 'FE - Flare ongoing at end of file'

def test_flag_meaning_fr():
    assert flag_meaning('FR') == 'FR - In Fast Rate Mode'

def test_flag_meaning_fs():
    assert flag_meaning('FS') == 'FS - Flare ongoing at start of file'

def test_flag_meaning_gd():
    assert flag_meaning('GD') == 'GD - Data gap during flare'

def test_flag_meaning_ge():
    assert flag_meaning('GE') == 'GE - Flare ended in data gap'

def test_flag_meaning_gs():
    assert flag_meaning('GS') == 'GS - Flare started in data gap'

def test_flag_meaning_mr():
    assert flag_meaning('MR') == 'MR - Spacecraft in high-latitude zone during flare'

def test_flag_meaning_ns():
    assert flag_meaning('NS') == 'NS - Non-solar event'

def test_flag_meaning_pe():
    assert flag_meaning('PE') == 'PE - Particle event: Particles are present'

def test_flag_meaning_ps():
    assert flag_meaning('PS') == 'PS - Possible Solar Flare; in front detectors, but no position'

def test_flag_meaning_pn():
    assert flag_meaning('Pn') == 'Pn - Position Quality: P0 = Position is NOT valid, P1 = Position is valid'

def test_flag_meaning_qn():
    assert flag_meaning('Qn') == 'Qn - Data Quality: Q0 = Highest Quality, Q11 = Lowest Quality'

def test_flag_meaning_sd():
    assert flag_meaning('SD') == 'SD - Spacecraft was in SAA sometime during flare'

def test_flag_meaning_se():
    assert flag_meaning('SE') == 'SE - Flare ended when spacecraft was in SAA'

def test_flag_meaning_ss():
    assert flag_meaning('SS') == 'SS - Flare started when spacecraft was in SAA'
