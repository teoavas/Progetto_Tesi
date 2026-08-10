from funzione import get_processor_types_from_config_class
import collections.abc

def test_get_processor_types_from_config_class_1():
    assert get_processor_types_from_config_class("BertConfig") == ("BertProcessor",)

def test_get_processor_types_from_config_class_2():
    assert get_processor_types_from_config_class("GPTConfig") == ("GPTProcessor", "GPTTokenizer")

def test_get_processor_types_from_config_class_3():
    assert get_processor_types_from_config_class("RobertaConfig") == ("RobertaProcessor",)

def test_get_processor_types_from_config_class_4():
    assert get_processor_types_from_config_class("XLNetConfig") == ("XLNetProcessor", "XLNetTokenizer")

def test_get_processor_types_from_config_class_5():
    assert get_processor_types_from_config_class("DistilBertConfig") == ("DistilBertProcessor", "DistilBertTokenizer")

def test_get_processor_types_from_config_class_6():
    assert get_processor_types_from_config_class("RobertaConfig", allowed_mappings=["image_processor"]) == ("RobertaImageProcessor",)

def test_get_processor_types_from_config_class_7():
    assert get_processor_types_from_config_class("GPTConfig", allowed_mappings=["feature_extractor"]) == ("GPTFeatureExtractor",)

def test_get_processor_types_from_config_class_8():
    assert get_processor_types_from_config_class("UnknownConfig") == ()
