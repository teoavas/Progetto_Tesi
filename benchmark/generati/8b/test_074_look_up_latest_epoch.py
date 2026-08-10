from funzione import look_up_latest_epoch
import os
import tempfile

def test_look_up_latest_epoch_1():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir, 'trained'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_supervised'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_supervised_parallel'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised', 'autoencoder_supervised_parallel'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised', 'autoencoder_supervised_parallel', 'epoch1.h5'))
        assert look_up_latest_epoch(0, -1, -1, tmpdir, 'modeltag', 'class_type', 'encoder_version') == (1, 1)

def test_look_up_latest_epoch_2():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir, 'trained'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_supervised'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_supervised_parallel'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised', 'autoencoder_supervised_parallel'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised', 'autoencoder_supervised_parallel', 'epoch1.h5'))
        assert look_up_latest_epoch(1, 1, -1, tmpdir, 'modeltag', 'class_type', 'encoder_version') == (1, 2)

def test_look_up_latest_epoch_3():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir, 'trained'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_supervised'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_supervised_parallel'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised', 'autoencoder_supervised_parallel'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised', 'autoencoder_supervised_parallel', 'epoch1.h5'))
        assert look_up_latest_epoch(2, 1, -1, tmpdir, 'modeltag', 'class_type', 'encoder_version') == (1, 1)

def test_look_up_latest_epoch_4():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir, 'trained'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_supervised'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_supervised_parallel'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised', 'autoencoder_supervised_parallel'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_epoch1.h5', 'supervised', 'autoencoder_supervised_parallel', 'epoch1.h5'))
        assert look_up_latest_epoch(3, 1, -1, tmpdir, 'modeltag', 'class_type', 'encoder_version') == (1, 1)

def test_look_up_latest_epoch_5():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir, 'trained'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder'))
        os.makedirs(os.path.join(tmpdir, 'trained', 'autoencoder_supervised'))
        os.makedirs(os.path.join(tmp
