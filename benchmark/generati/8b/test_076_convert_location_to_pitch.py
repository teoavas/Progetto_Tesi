from funzione import convert_location_to_pitch

def test_convert_location_to_pitch_1():
    assert convert_location_to_pitch('clef-G2', 0) == 'note-C2'

def test_convert_location_to_pitch_2():
    assert convert_location_to_pitch('clef-G2', 1) == 'note-D2'

def test_convert_location_to_pitch_3():
    assert convert_location_to_pitch('clef-G2', 2) == 'note-E2'

def test_convert_location_to_pitch_4():
    assert convert_location_to_pitch('clef-G2', 3) == 'note-F2'

def test_convert_location_to_pitch_5():
    assert convert_location_to_pitch('clef-G2', 4) == 'note-G2'

def test_convert_location_to_pitch_6():
    assert convert_location_to_pitch('clef-G2', 5) == 'note-A2'

def test_convert_location_to_pitch_7():
    assert convert_location_to_pitch('clef-G2', 6) == 'note-B2'

def test_convert_location_to_pitch_8():
    assert convert_location_to_pitch('clef-G2', 7) == 'note-C3'

def test_convert_location_to_pitch_9():
    assert convert_location_to_pitch('clef-G2', 8) == 'note-D3'

def test_convert_location_to_pitch_10():
    assert convert_location_to_pitch('clef-G2', 9) == 'note-E3'

def test_convert_location_to_pitch_11():
    assert convert_location_to_pitch('clef-G2', 10) == 'note-F3'

def test_convert_location_to_pitch_12():
    assert convert_location_to_pitch('clef-G2', 11) == 'note-G3'

def test_convert_location_to_pitch_13():
    assert convert_location_to_pitch('clef-G2', 12) == 'note-A3'

def test_convert_location_to_pitch_14():
    assert convert_location_to_pitch('clef-G2', 13) == 'note-B3'

def test_convert_location_to_pitch_15():
    assert convert_location_to_pitch('clef-G2', 14) == 'note-C4'

def test_convert_location_to_pitch_16():
    assert convert_location_to_pitch('clef-G2', 15) == 'note-D4'

def test_convert_location_to_pitch_17():
    assert convert_location_to_pitch('clef-G2', 16) == 'note-E4'

def test_convert_location_to_pitch_18():
    assert convert_location_to_pitch('clef-G2', 17) == 'note-F4'

def test_convert_location_to_pitch_19():
    assert convert_location_to_pitch('clef-G2', 18) == 'note-G4'

def test_convert_location_to_pitch_20():
    assert convert_location_to_pitch('clef-G2', 19) == 'note-A4'

def test_convert_location_to_pitch_21():
    assert convert_location_to_pitch('clef-G2', 20) == 'note-B4'

def test_convert_location_to_pitch_22():
    assert convert_location_to_pitch('clef-G2', 21) == 'note-C5'

def test_convert_location_to_pitch_23():
    assert convert_location_to_pitch('clef-G2', 22) == 'note-D5'

def test_convert_location_to_pitch_24():
    assert convert_location_to_pitch('clef-G2', 23) == 'note-E5'

def test_convert_location_to_pitch_25():
    assert convert_location_to_pitch('clef-G2', 24) == 'note-F5'

def test_convert_location_to_pitch_26():
    assert convert_location_to_pitch('clef-G2', 25) == 'note-G5'

def test_convert_location_to_pitch_27():
    assert convert_location_to_pitch('clef-G2', 26) == 'note-A5'

def test_convert_location_to_pitch_28():
    assert convert_location_to_pitch('clef-G2', 27) == 'note-B5'

def test_convert_location_to_pitch_29():
    assert convert_location_to_pitch('clef-G2', 28) == 'note-C6'

def test_convert_location_to_pitch_30():
    assert convert_location_to_pitch('clef-G2', 29) == 'note-D6'

def test_convert_location_to_pitch_31():
    assert convert_location_to_pitch('clef-G2', 30) == 'note-E6'

def test_convert_location_to_pitch_32():
    assert convert_location_to_pitch('clef-G2', 31) == 'note-F6'

def test_convert_location_to_pitch_33():
    assert convert_location_to_pitch('clef-G2', 32) == 'note-G6'

def test_convert_location_to_pitch_34():
    assert convert_location_to_pitch('clef-G2', 33) ==
