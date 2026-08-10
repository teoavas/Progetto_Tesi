from funzione import _normalized_vcf

def test__normalized_vcf_1():
    assert _normalized_vcf('chr1', 100, 'A', 'T') == ('chr1', 100, 'A', 'T')

def test__normalized_vcf_2():
    assert _normalized_vcf('chr1', 100, 'AA', 'T') == ('chr1', 101, 'A', 'T')

def test__normalized_vcf_3():
    assert _normalized_vcf('chr1', 100, 'A', 'AA') == ('chr1', 100, 'A', 'AA')

def test__normalized_vcf_4():
    assert _normalized_vcf('chr1', 100, 'AA', 'AA') == ('chr1', 100, 'AA', 'AA')

def test__normalized_vcf_5():
    with pytest.raises(ValueError):
        _normalized_vcf('chr1', 100, 'AA', 'AA')

def test__normalized_vcf_6():
    with pytest.raises(ValueError):
        _normalized_vcf('chr1', 100, 'A', 'A')

def test__normalized_vcf_7():
    assert _normalized_vcf('chr1', 100, 'A', 'T') == ('chr1', 100, 'A', 'T')
