import pytest
import os
from funzione import look_up_latest_epoch

@pytest.fixture
def mock_model_folder():
    return 'path/to/model/folder'

@pytest.fixture
def mock_modeltag():
    return 'model_tag'

@pytest.fixture
def mock_class_type():
    return ('class_name', '')

@pytest.fixture
def mock_encoder_version():
    return 'encoder_version'

def test_look_up_latest_epoch_1(mock_model_folder, mock_modeltag):
    epoch, encoder_epoch = look_up_latest_epoch(0, -1, -1, mock_model_folder, mock_modeltag, mock_class_type(), mock_encoder_version())
    assert epoch == 10
    assert os.path.isfile(f'{mock_model_folder}trained_{mock_modeltag}_autoencoder_epoch{epoch+1}.h5') == True

def test_look_up_latest_epoch_2(mock_model_folder, mock_modeltag):
    epoch, encoder_epoch = look_up_latest_epoch(1, 0, -1, mock_model_folder, mock_modeltag, mock_class_type(), mock_encoder_version())
    assert epoch == 0
    assert os.path.isfile(f'{mock_model_folder}trained_{mock_modeltag}_autoencoder_epoch{epoch+1}.h5') == True

def test_look_up_latest_epoch_3(mock_model_folder, mock_modeltag):
    epoch, encoder_epoch = look_up_latest_epoch(2, -1, -1, mock_model_folder, mock_modeltag, mock_class_type(), mock_encoder_version())
    assert epoch == 10
    assert os.path.isfile(f'{mock_model_folder}trained_{mock_modeltag}_supervised_{mock_class_type()[1]}{mock_encoder_version()}epoch{epoch+1}.h5') == True

def test_look_up_latest_epoch_4(mock_model_folder, mock_modeltag):
    epoch, encoder_epoch = look_up_latest_epoch(3, -1, -1, mock_model_folder, mock_modeltag, mock_class_type(), mock_encoder_version())
    assert epoch == 10
    assert os.path.isfile(f'{mock_model_folder}trained_{mock_modeltag}_autoencoder_supervised_parallel_{mock_class_type()[1]}{mock_encoder_version()}epoch{epoch+1}.h5') == True

def test_look_up_latest_epoch_5(mock_model_folder, mock_modeltag):
    epoch, encoder_epoch = look_up_latest_epoch(0, -1, 10, mock_model_folder, mock_modeltag, mock_class_type(), mock_encoder_version())
    assert epoch == 11
    assert os.path.isfile(f'{mock_model_folder}trained_{mock_modeltag}_autoencoder_epoch{epoch+1}.h5') == True

def test_look_up_latest_epoch_6(mock_model_folder, mock_modeltag):
    epoch, encoder_epoch = look_up_latest_epoch(1, 0, -1, mock_model_folder, mock_modeltag, mock_class_type(), mock_encoder_version())
    assert epoch == 0
    assert os.path.isfile(f'{mock_model_folder}trained_{mock_modeltag}_autoencoder_epoch{epoch+1}.h5') == True

def test_look_up_latest_epoch_7(mock_model_folder, mock_modeltag):
    epoch, encoder_epoch = look_up_latest_epoch(2, -1, 10, mock_model_folder, mock_modeltag, mock_class_type(), mock_encoder_version())
    assert epoch == 11
    assert os.path.isfile(f'{mock_model_folder}trained_{mock_modeltag}_supervised_{mock_class_type()[1]}{mock_encoder_version()}epoch{epoch+1}.h5') == True

def test_look_up_latest_epoch_8(mock_model_folder, mock_modeltag):
    epoch, encoder_epoch = look_up_latest_epoch(3, -1, 10, mock_model_folder, mock_modeltag, mock_class_type(), mock_encoder_version())
    assert epoch == 11
    assert os.path.isfile(f'{mock_model_folder}trained_{mock_modeltag}_autoencoder_supervised_parallel_{mock_class_type()[1]}{mock_encoder_version()}epoch{epoch+1}.h5') == True
