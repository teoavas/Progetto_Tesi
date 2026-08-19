import pytest
from funzione import get_processor_types_from_config_class

@pytest.mark.parametrize("config_class", ["BertConfig", "GPTConfig"])
def test_get_processor_types_from_config_class_1(config_class):
    processor_types = get_processor_types_from_config_class(config_class)
    assert isinstance(processor_types, tuple)

@pytest.mark.parametrize("config_class", ["BertConfig", "DistilBertConfig"])
def test_get_processor_types_from_config_class_2(config_class):
    processor_types = get_processor_types_from_config_class(config_class)
    assert len(processor_types) == 1

@pytest.mark.parametrize("config_class", ["GPTConfig", "XLNetConfig"])
def test_get_processor_types_from_config_class_3(config_class):
    processor_types = get_processor_types_from_config_class(config_class)
    assert isinstance(processor_types, tuple)

@pytest.mark.parametrize("config_class", ["BertConfig", "RobertaConfig"])
def test_get_processor_types_from_config_class_4(config_class):
    processor_types = get_processor_types_from_config_class(config_class)
    assert len(processor_types) == 2

@pytest.mark.parametrize("config_class", ["GPTConfig", "DistilBertConfig"])
def test_get_processor_types_from_config_class_5(config_class):
    processor_types = get_processor_types_from_config_class(config_class)
    assert isinstance(processor_types, tuple)

@pytest.mark.parametrize("config_class", ["XLNetConfig", "RobertaConfig"])
def test_get_processor_types_from_config_class_6(config_class):
    processor_types = get_processor_types_from_config_class(config_class)
    assert len(processor_types) == 2

@pytest.mark.parametrize("config_class", ["BertConfig", "GPTConfig", "DistilBertConfig"])
def test_get_processor_types_from_config_class_7(config_class):
    processor_types = get_processor_types_from_config_class(config_class)
    assert isinstance(processor_types, tuple)

@pytest.mark.parametrize("config_class", ["RobertaConfig", "XLNetConfig"])
def test_get_processor_types_from_config_class_8(config_class):
    processor_types = get_processor_types_from_config_class(config_class)
    assert len(processor_types) == 2

def test_get_processor_types_from_config_class_no_mappings():
    assert get_processor_types_from_config_class("CustomConfig") is None
