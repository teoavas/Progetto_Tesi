from funzione import look_up_latest_epoch
import os

def test_look_up_latest_epoch_1():
    assert look_up_latest_epoch(0, -1, 0, '/path/to/model/folder', 'modeltag', ['class_type'], 'encoder_version') == (0, 0)

def test_look_up_latest_epoch_2():
    assert look_up_latest_epoch(1, -1, 0, '/path/to/model/folder', 'modeltag', ['class_type'], 'encoder_version') == (0, 0)

def test_look_up_latest_epoch_3():
    assert look_up_latest_epoch(2, -1, 0, '/path/to/model/folder', 'modeltag', ['class_type'], 'encoder_version') == (0, 0)

def test_look_up_latest_epoch_4():
    assert look_up_latest_epoch(3, -1, 0, '/path/to/model/folder', 'modeltag', ['class_type'], 'encoder_version') == (0, 0)

def test_look_up_latest_epoch_5():
    os.makedirs('/path/to/model/folder/trained_modeltag_autoencoder_epoch1.h5')
    assert look_up_latest_epoch(0, -1, 0, '/path/to/model/folder', 'modeltag', ['class_type'], 'encoder_version') == (1, 0)

def test_look_up_latest_epoch_6():
    os.makedirs('/path/to/model/folder/trained_modeltag_autoencoder_epoch1.h5')
    os.makedirs('/path/to/model/folder/trained_modeltag_autoencoder_epoch2.h5')
    assert look_up_latest_epoch(0, -1, 0, '/path/to/model/folder', 'modeltag', ['class_type'], 'encoder_version') == (2, 0)

def test_look_up_latest_epoch_7():
    os.makedirs('/path/to/model/folder/trained_modeltag_autoencoder_epoch1.h5')
    os.makedirs('/path/to/model/folder/trained_modeltag_autoencoder_epoch2.h5')
    os.makedirs('/path/to/model/folder/trained_modeltag_autoencoder_epoch3.h5')
    assert look_up_latest_epoch(0, -1, 0, '/path/to/model/folder', 'modeltag', ['class_type'], 'encoder_version') == (3, 0)
