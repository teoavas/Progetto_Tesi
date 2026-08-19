from funzione import _normalized_vcf

def test__normalized_vcf_1():
    chr = 'chr1'
    pos = 100
    ref = 'A'
    alt = 'G'
    assert _normalized_vcf(chr, pos, ref, alt) == (chr, pos + 0, ref[0], alt[0])

def test__normalized_vcf_2():
    chr = 'chr1'
    pos = 100
    ref = 'AA'
    alt = 'GG'
    assert _normalized_vcf(chr, pos, ref, alt) == (chr, pos + 1, ref[1:], alt[1:])

def test__normalized_vcf_3():
    chr = 'chr1'
    pos = 100
    ref = 'A'
    alt = 'GGG'
    assert _normalized_vcf(chr, pos, ref, alt) == (chr, pos + 2, ref[0], alt[0:2])

def test__normalized_vcf_4():
    chr = 'chr1'
    pos = 100
    ref = 'AA'
    alt = 'G'
    assert _normalized_vcf(chr, pos, ref, alt) == (chr, pos + 1, ref[1:], alt)

def test__normalized_vcf_5():
    chr = 'chr1'
    pos = 100
    ref = None
    alt = 'GGG'
    with pytest.raises(ValueError):
        _normalized_vcf(chr, pos, ref, alt)

def test__normalized_vcf_6():
    chr = 'chr1'
    pos = 100
    ref = 'AA'
    alt = None
    with pytest.raises(ValueError):
        _normalized_vcf(chr, pos, ref, alt)
