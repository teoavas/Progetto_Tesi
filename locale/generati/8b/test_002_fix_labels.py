from funzione import fix_labels
import re

def test_fix_labels_1():
    header = ["Unix", "Accel_X", "Gyro_Y"]
    expected_header = ["Timestamp", "Accel_X", "Gyro_Y"]
    assert fix_labels(header) == expected_header

def test_fix_labels_2():
    header = ["Pressure", "Temp", "GSR"]
    expected_header = ["Pressure", "Temperature", "GSR"]
    assert fix_labels(header) == expected_header

def test_fix_labels_3():
    header = ["Unix", "Accel_X", "Gyro_Y", "Pressure", "Temp", "GSR"]
    expected_header = ["Timestamp", "Accel_X", "Gyro_Y", "Pressure", "Temperature", "GSR"]
    assert fix_labels(header) == expected_header

def test_fix_labels_4():
    header = ["Unix", "Accel_X", "Gyro_Y", "Pressure", "Temp", "GSR", "Invalid_Label"]
    expected_header = ["Timestamp", "Accel_X", "Gyro_Y", "Pressure", "Temperature", "GSR", "Invalid_Label"]
    assert fix_labels(header) == expected_header

def test_fix_labels_5():
    header = []
    expected_header = []
    assert fix_labels(header) == expected_header

def test_fix_labels_6():
    header = ["Unix", "Accel_X", "Gyro_Y", "Pressure", "Temp", "GSR"]
    expected_header = ["Timestamp", "Accel_X", "Gyro_Y", "Pressure", "Temperature", "GSR"]
    assert fix_labels(header) == expected_header

def test_fix_labels_7():
    header = ["Invalid_Label", "Unix", "Accel_X", "Gyro_Y", "Pressure", "Temp", "GSR"]
    expected_header = ["Unix", "Timestamp", "Accel_X", "Gyro_Y", "Pressure", "Temperature", "GSR"]
    assert fix_labels(header) == expected_header
