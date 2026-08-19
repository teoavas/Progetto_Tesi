from funzione import _normalized_vcf

def test__normalized_vcf_1():
    assert _normalized_vcf('chr1', '10:20', 'A', 'T') == ('chr1', 21, 'A', 'T')

def test__normalized_vcf_2():
    with pytest.raises(ValueError):
        _normalized_vcf('chr1', '10:20', 'A', 'A')

def test__normalized_vcf_3():
    assert _normalized_vcf('chr1', '10:20', 'AT', 'T') == ('chr1', 21, 'T', 'T')

def test__normalized_vcf_4():
    with pytest.raises(ValueError):
        _normalized_vcf('chr1', '10:20', None, None)

def test__normalized_vcf_5():
    assert _normalized_vcf('chr1', '10:20', 'A', None) == ('chr1', 21, 'A', None)
    assert _normalized_vcf('chr1', '10:20', None, 'T') == ('chr1', 21, None, 'T')

def test__normalized_vcf_6():
    assert _normalized_vcf('chr1', '10:20', 'AT', 'AC') == ('chr1', 22, 'A', 'C')

def test__normalized_vcf_7():
    with pytest.raises(ValueError):
        _normalized_vcf('chr1', '10:20', 'AT', 'TT')
