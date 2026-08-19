import pytest
from funzione import convert_location_to_pitch

@pytest.mark.parametrize("clef", ["clef-G2", "clef-F4"])
def test_convert_location_to_pitch_1(clef):
    assert convert_location_to_pitch(clef, 0) in ['rest', 'note-0 note-1']

@pytest.mark.parametrize("clef", ["clef-C3", "clef-C5"])
def test_convert_location_to_pitch_2(clef):
    assert convert_location_to_pitch(clef, 4) == 'note-4 note-5'

@pytest.mark.parametrize("clef", ["clef-G2", "clef-F4", "clef-C3"])
def test_convert_location_to_pitch_3(clef):
    assert convert_location_to_pitch(clef, 0) in ['rest', 'note-1 note-2']

@pytest.mark.parametrize("clef", ["clef-G2", "clef-F4", "clef-C5"])
def test_convert_location_to_pitch_4(clef):
    assert convert_location_to_pitch(clef, 3) == 'note-3 note-4'

@pytest.mark.parametrize("clef", ["clef-G1", "clef-F3", "clef-C2"])
def test_convert_location_to_pitch_5(clef):
    assert convert_location_to_pitch(clef, 0) in ['rest', 'note-1 note-2']

@pytest.mark.parametrize("clef", ["clef-G2", "clef-F4", "clef-C3", "clef-C5"])
def test_convert_location_to_pitch_6(clef):
    assert convert_location_to_pitch(clef, 0) in ['rest', 'note-1 note-2']

@pytest.mark.parametrize("clef", ["clef-G2", "clef-F4", "clef-C3", "clef-C5"])
def test_convert_location_to_pitch_7(clef):
    assert convert_location_to_pitch(clef, 6) in ['rest', 'note-0 note-1']
