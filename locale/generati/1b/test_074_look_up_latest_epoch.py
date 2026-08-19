import os
import pytest
from funzione import look_up_latest_epoch

def test_look_up_latest_epoch_1():
    assert look_up_latest_epoch(0, -1, 0, 'model_folder', 'modeltag', ['class_type'], 'encoder_version') == (0, 0)

def test_look_up_latest_epoch_2():
    assert look_up_latest_epoch(1, -1, 0, 'model_folder', 'modeltag', ['class_type'], 'encoder_version') == (1, 0)

def test_look_up_latest_epoch_3():
    assert look_up_latest_epoch(2, -1, 0, 'model_folder', 'modeltag', ['class_type'], 'encoder_version') == (2, 0)

def test_look_up_latest_epoch_4():
    assert look_up_latest_epoch(3, -1, 0, 'model_folder', 'modeltag', ['class_type'], 'encoder_version') == (3, 0)

def test_look_up_latest_epoch_5():
    assert look_up_latest_epoch(0, -2, 0, 'model_folder', 'modeltag', ['class_type'], 'encoder_version') == (1, 0)

def test_look_up_latest_epoch_6():
    assert look_up_latest_epoch(1, -2, 0, 'model_folder', 'modeltag', ['class_type'], 'encoder_version') == (2, 0)

def test_look_up_latest_epoch_7():
    assert look_up_latest_epoch(2, -2, 0, 'model_folder', 'modeltag', ['class_type'], 'encoder_version') == (3, 0)
