import pytest

def test__normalized_vcf_1():
    assert _normalized_vcf('A', 100, 'G', 'C') == ('A', 101, 'G', 'C')

def test__normalized_vcf_2():
    with pytest.raises(ValueError):
        _normalized_vcf('A', 100, 'G', 'T')

def test__normalized_vcf_3():
    assert _normalized_vcf('A', 100, 'G', '') == ('A', 101, 'G', '')

def test__normalized_vcf_4():
    assert _normalized_vcf('A', 100, '', 'C') == ('A', 101, '', 'C')

def test__normalized_vcf_5():
    with pytest.raises(ValueError):
        _normalized_vcf('', 100, 'G', 'T')

def test__normalized_vcf_6():
    assert _normalized_vcf('A', -1, 'G', '') == ('A', -1, 'G', '')

def test__normalized_vcf_7():
    with pytest.raises(ValueError):
        _normalized_vcf('A', 100, '', '')

def test__normalized_vcf_8():
    assert _normalized_vcf('A', 100, 'G', 'C') == ('A', 101, 'G', 'C')
