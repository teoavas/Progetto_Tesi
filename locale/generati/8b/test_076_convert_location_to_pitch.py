from funzione import convert_location_to_pitch

def test_convert_location_to_pitch_1():
    assert convert_location_to_pitch('clef-G2', 0) == 'note-C3'

def test_convert_location_to_pitch_2():
    assert convert_location_to_pitch('clef-G2', 1) == 'note-D3'

def test_convert_location_to_pitch_3():
    assert convert_location_to_pitch('clef-G2', 2) == 'note-E3'

def test_convert_location_to_pitch_4():
    assert convert_location_to_pitch('clef-G2', 86) == 'rest'

def test_convert_location_to_pitch_5():
    assert convert_location_to_pitch('clef-F4', 0) == 'note-C1'

def test_convert_location_to_pitch_6():
    assert convert_location_to_pitch('clef-F4', 3) == 'note-F1'

def test_convert_location_to_pitch_7():
    assert convert_location_to_pitch('clef-G2', 85) == 'rest'
