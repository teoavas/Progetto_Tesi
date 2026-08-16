import re
from pytest import fixture, mark

@fixture
def header():
    return ["Unix", "Accel_X", "Gyro_X", "Pressure"]

def test_fix_labels_1(header):
    assert fix_labels(header) == ["Timestamp", "Accel_X", "Gyro_X", "Pressure"]

def test_fix_labels_2(header):
    assert fix_labels(header) == ["Timestamp", "Accel_Y", "Gyro_Y", "Pressure"]

def test_fix_labels_3(header):
    assert fix_labels(header) == ["Timestamp", "Accel_Z", "Gyro_Z", "Pressure"]

def test_fix_labels_4(header):
    assert fix_labels(header) == ["Timestamp", "Accel_X", "Gyro_X", "Pressure", "Temp"]

def test_fix_labels_5(header):
    assert fix_labels(header) == ["Timestamp", "Accel_Y", "Gyro_Y", "Pressure", "Temp"]

@mark.parametrize("i", range(1, 6))
def test_fix_labels_6(i, header):
    assert header[i] in ["Timestamp", "Accel_X", "Gyro_X", "Pressure", "Temp"]

def test_fix_labels_7(header):
    assert re.search("Unix", header[0]) is not None
