from funzione import fileNamer

def test_fileNamer_1():
    assert fileNamer(node_model=True) == 'NodeModel'

def test_fileNamer_2():
    assert fileNamer(node_model=False) == 'EdgeModel'

def test_fileNamer_3():
    assert fileNamer(l_inf=0.5) == 'Linf0.5'

def test_fileNamer_4():
    assert fileNamer(l_0=0.5) == 'AttrRatio0.5'

def test_fileNamer_5():
    assert fileNamer(num_layers=5) == '5Layers'

def test_fileNamer_6():
    assert fileNamer(seed=42) == 'Seed42'

def test_fileNamer_7():
    assert fileNamer(targeted=False) == 'untargeted'
    assert fileNamer(targeted=True) == 'targeted'

def test_fileNamer_8():
    assert fileNamer(continuous_epochs=1000) == '1000K'
    assert fileNamer(patience=5) == 'patience5'

def test_fileNamer_9():
    assert fileNamer(start='start', end='end') == 'start_NodeModel_dataset_name_model_name_5Layers_Seed42_Linf0.5_AttrRatio0.5_untargeted_1000K_patience5_end'

def test_fileNamer_10():
    assert fileNamer(node_model=True, dataset_name='dataset_name', model_name='model_name') == 'NodeModel_dataset_name_model_name_5Layers_Seed42_Linf0.5_AttrRatio0.5_untargeted_1000K_patience5'
