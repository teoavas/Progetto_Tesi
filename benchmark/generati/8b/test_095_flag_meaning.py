from funzione import flag_meaning

def test_flag_meaning_1():
    assert flag_meaning('all') == "Flare Flag Codes: \na0 - In attenuator state 0 (None) sometime during flare \na1 - In attenuator state 1 (Thin) sometime during flare \na2 - In attenuator state 2 (Thick) sometime during flare \na3 - In attenuator state 3 (Both) sometime during flare \nAn - Attenuator state (0=None, 1=Thin, 2=Thick, 3=Both) at peak of flare \nDF - Front segment counts were decimated sometime during flare\nDR - Rear segment counts were decimated sometime during flare \nED - Spacecraft eclipse (night) sometime during flare\nEE - Flare ended in spacecraft eclipse (night) \nES - Flare started in spacecraft eclipse (night) \nFE - Flare ongoing at end of file \nFR - In Fast Rate Mode \nFS - Flare ongoing at start of file \nGD - Data gap during flare \nGE - Flare ended in data gap\nGS - Flare started in data gap \nMR - Spacecraft in high-latitude zone during flare \nNS - Non-solar event\nPE - Particle event: Particles are present \nPS - Possible Solar Flare; in front detectors, but no position\nPn - Position Quality: P0 = Position is NOT valid, P1 = Position is valid \nQn - Data Quality: Q0 = Highest Quality, Q11 = Lowest Quality\nSD - Spacecraft was in SAA sometime during flare \nSE - Flare ended when spacecraft was in SAA\nSS - Flare started when spacecraft was in SAA"

def test_flag_meaning_2():
    assert flag_meaning('a0') == 'a0 - In attenuator state 0 (None) sometime during flare'

def test_flag_meaning_3():
    assert flag_meaning('a1') == 'a1 - In attenuator state 1 (Thin) sometime during flare'

def test_flag_meaning_4():
    assert flag_meaning('a2') == 'a2 - In attenuator state 2 (Thick) sometime during flare'

def test_flag_meaning_5():
    assert flag_meaning('a3') == 'a3 - In attenuator state 3 (Both) sometime during flare'

def test_flag_meaning_6():
    assert flag_meaning('A1') == 'An - Attenuator state (0=None, 1=Thin, 2=Thick, 3=Both) at peak of flare'

def test_flag_meaning_7():
    assert flag_meaning('DF') == 'DF - Front segment counts were decimated sometime during flare'

def test_flag_meaning_8():
    assert flag_meaning('DR') == 'DR - Rear segment counts were decimated sometime during flare'

def test_flag_meaning_9():
    assert flag_meaning('ED') == 'ED - Spacecraft eclipse (night) sometime during flare'

def test_flag_meaning_10():
    assert flag_meaning('EE') == 'EE - Flare ended in spacecraft eclipse (night)'

def test_flag_meaning_11():
    assert flag_meaning('ES') == 'ES - Flare started in spacecraft eclipse (night)'

def test_flag_meaning_12():
    assert flag_meaning('FE') == 'FE - Flare ongoing at end of file'

def test_flag_meaning_13():
    assert flag_meaning('FR') == 'FR - In Fast Rate Mode'

def test_flag_meaning_14():
    assert flag_meaning('FS') == 'FS - Flare ongoing at start of file'

def test_flag_meaning_15():
    assert flag_meaning('GD') == 'GD - Data gap during flare'

def test_flag_meaning_16():
    assert flag_meaning('GE') == 'GE - Flare ended in data gap'

def test_flag_meaning_17():
    assert flag_meaning('GS') == 'GS - Flare started in data gap'

def test_flag_meaning_18():
    assert flag_meaning('MR') == 'MR - Spacecraft in high-latitude zone during flare'

def test_flag_meaning_19():
    assert flag_meaning('NS') == 'NS - Non-solar event'

def test_flag_meaning_20():
    assert flag_meaning('PE') == 'PE - Particle event: Particles are present'

def test_flag_meaning_21():
    assert flag_meaning('PS') == 'PS - Possible Solar Flare; in front detectors, but no position'

def test_flag_meaning_22():
    assert flag_meaning('P1') == 'Pn - Position Quality: P0 = Position is NOT valid, P
