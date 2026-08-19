from funzione import convert_location_to_pitch

def test_convert_location_to_pitch_1():
    assert convert_location_to_pitch('clef-G2', 0) == 'note-D-2'

def test_convert_location_to_pitch_2():
    assert convert_location_to_pitch('clef-G1', 3) == 'note-F-2'

def test_convert_location_to_pitch_3():
    assert convert_location_to_pitch('clef-F4', 5) == 'note-A-0'

def test_convert_location_to_pitch_4():
    assert convert_location_to_pitch('clef-C3', 1) == 'note-E-1'

def test_convert_location_to_pitch_5():
    assert convert_location_to_pitch('clef-C4', 2) == 'note-G-1'

def test_convert_location_to_pitch_6():
    assert convert_location_to_pitch('clef-F5', 0) == 'note-D-0'

def test_convert_location_to_pitch_7():
    assert convert_location_to_pitch('clef-C1', 4) == 'note-B-1'
