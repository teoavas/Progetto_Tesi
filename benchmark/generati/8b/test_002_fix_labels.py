import pytest
import re

from funzione import fix_labels

def test_fix_labels_1():
    header = ["Unix", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temp", "GSR"]
    expected = ["Timestamp", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temperature", "GSR"]
    assert fix_labels(header) == expected

def test_fix_labels_2():
    header = ["Unix", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temp", "GSR", "Unix"]
    expected = ["Timestamp", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temperature", "GSR", "Timestamp"]
    assert fix_labels(header) == expected

def test_fix_labels_3():
    header = ["Unix", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temp", "GSR", "Other"]
    expected = ["Timestamp", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temperature", "GSR"]
    assert fix_labels(header) == expected

def test_fix_labels_4():
    header = ["Unix", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temp", "GSR", "Unix", "Other"]
    expected = ["Timestamp", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temperature", "GSR", "Timestamp", "Other"]
    assert fix_labels(header) == expected

def test_fix_labels_5():
    header = ["Unix", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temp", "GSR", "Unix", "Other", "Other"]
    expected = ["Timestamp", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temperature", "GSR", "Timestamp", "Other", "Other"]
    assert fix_labels(header) == expected

def test_fix_labels_6():
    header = ["Unix", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temp", "GSR", "Unix", "Other", "Other", "Other"]
    expected = ["Timestamp", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temperature", "GSR", "Timestamp", "Other", "Other", "Other"]
    assert fix_labels(header) == expected

def test_fix_labels_7():
    header = []
    expected = []
    assert fix_labels(header) == expected

def test_fix_labels_8():
    header = ["Unix", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temp", "GSR"]
    expected = ["Timestamp", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z", "Pressure", "Temperature", "GSR"]
    assert fix_labels(header) == expected
