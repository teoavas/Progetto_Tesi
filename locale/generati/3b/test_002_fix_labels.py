from funzione import fix_labels
import re

def test_fix_labels_1():
    assert fix_labels(["Unix Time"]) == ["Timestamp"]

def test_fix_labels_2():
    assert fix_labels(["Accel X", "Gyro Y"]) == ["Accel_X", "Gyro_Y"]

def test_fix_labels_3():
    assert fix_labels(["Pressure", "Temp"]) == ["Pressure", "Temperature"]

def test_fix_labels_4():
    assert fix_labels(["GSR", "Unix Time"]) == ["GSR", "Timestamp"]

def test_fix_labels_5():
    assert fix_labels(["Accel X", "Gyro Z"]) == ["Accel_X", "Gyro_Z"]

def test_fix_labels_6():
    assert fix_labels(["Temp", "Pressure"]) == ["Temperature", "Pressure"]

def test_fix_labels_7():
    assert fix_labels(["Unix Time", "GSR"]) == ["Timestamp", "GSR"]

def test_fix_labels_8():
    assert fix_labels(["Accel X", "Gyro Y", "Pressure"]) == ["Accel_X", "Gyro_Y", "Pressure"]
