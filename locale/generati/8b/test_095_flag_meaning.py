from funzione import flag_meaning

def test_flag_meaning_1():
    assert flag_meaning('all') == "Flare Flag Codes: \na0 - In attenuator state 0 (None) sometime during flare \na1 - In attenuator state 1 (Thin) sometime during flare \na2 - In attenuator state 2 (Thick) sometime during flare \na3 - In attenuator state 3 (Both) sometime during flare \nAn - Attenuator state (0=None, 1=Thin, 2=Thick, 3=Both) at peak of flare \nDF - Front segment counts were decimated sometime during flare\nDR - Rear segment counts were decimated sometime during flare \nED - Spacecraft eclipse (night) sometime during flare\nEE - Flare ended in spacecraft eclipse (night) \nES - Flare started in spacecraft eclipse (night) \nFE - Flare ongoing at end of file \nFR - In Fast Rate Mode \nFS - Flare ongoing at start of file \nGD - Data gap during flare \nGE - Flare ended in data gap\nGS - Flare started in data gap \nMR - Spacecraft in high-latitude zone during flare \nNS - Non-solar event\nPE - Particle event: Particles are present \nPS - Possible Solar Flare; in front detectors, but no position\nPn - Position Quality: P0 = Position is NOT valid, P1 = Position is valid \nQn - Data Quality: Q0 = Highest Quality, Q11 = Lowest Quality\nSD - Spacecraft was in SAA sometime during flare \nSE - Flare ended when spacecraft was in SAA\nSS - Flare started when spacecraft was in SAA"

def test_flag_meaning_2():
    assert flag_meaning('a0') == 'a0 - In attenuator state 0 (None) sometime during flare'

def test_flag_meaning_3():
    assert flag_meaning('DF') == 'DF - Front segment counts were decimated sometime during flare'

def test_flag_meaning_4():
    assert flag_meaning('Pn') == 'Pn - Position Quality: P0 = Position is NOT valid, P1 = Position is valid'

def test_flag_meaning_5():
    assert flag_meaning('Qn') == 'Qn - Data Quality: Q0 = Highest Quality, Q11 = Lowest Quality'

def test_flag_meaning_6():
    assert flag_meaning('invalid') == 'Error: invalid flag'

def test_flag_meaning_7():
    assert flag_meaning('a1') == 'a1 - In attenuator state 1 (Thin) sometime during flare'
