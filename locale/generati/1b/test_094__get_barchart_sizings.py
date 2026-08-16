test__get_barchart_sizings_1.py
import pytest

def test__get_barchart_sizings_1():
    width, xgap, xfontsize, minor_ticks, init_margin_offset_l = _get_barchart_sizings('x_title', 3, 5, 400)
    assert width > 1200 and xgap < 25 and xfontsize >= 10 and minor_ticks == 'true' and init_margin_offset_l == 35

test__get_barchart_sizings_2.py
import pytest

def test__get_barchart_sizings_2():
    width, xgap, xfontsize, minor_ticks, init_margin_offset_l = _get_barchart_sizings('x_title', 5, 8, 500)
    assert width > 1200 and xgap < 25 and xfontsize >= 10 and minor_ticks == 'true' and init_margin_offset_l == 35

test__get_barchart_sizings_3.py
import pytest

def test__get_barchart_sizings_3():
    width, xgap, xfontsize, minor_ticks, init_margin_offset_l = _get_barchart_sizings('x_title', 8, 10, 600)
    assert width > 1200 and xgap < 25 and xfontsize >= 9 and minor_ticks == 'true' and init_margin_offset_l == 35

test__get_barchart_sizings_4.py
import pytest

def test__get_barchart_sizings_4():
    width, xgap, xfontsize, minor_ticks, init_margin_offset_l = _get_barchart_sizings('x_title', 10, 16, 800)
    assert width > 1200 and xgap < 25 and xfontsize >= 8 and minor_ticks == 'true' and init_margin_offset_l == 35

test__get_barchart_sizings_5.py
import pytest

def test__get_barchart_sizings_5():
    width, xgap, xfontsize, minor_ticks, init_margin_offset_l = _get_barchart_sizings('x_title', 16, 20, 1000)
    assert width > 1200 and xgap < 25 and xfontsize >= 7 and minor_ticks == 'true' and init_margin_offset_l == 35

test__get_barchart_sizings_6.py
import pytest

def test__get_barchart_sizings_6():
    width, xgap, xfontsize, minor_ticks, init_margin_offset_l = _get_barchart_sizings('x_title', 20, 25, 1200)
    assert width > 1200 and xgap < 25 and xfontsize >= 10 and minor_ticks == 'true' and init_margin_offset_l == 35

test__get_barchart_sizings_7.py
import pytest

def test__get_barchart_sizings_7():
    width, xgap, xfontsize, minor_ticks, init_margin_offset_l = _get_barchart_sizings('x_title', 25, 30, 1500)
    assert width > 1200 and xgap < 25 and xfontsize >= 9 and minor_ticks == 'true' and init_margin_offset_l == 35

test__get_barchart_sizings_8.py
import pytest

def test__get_barchart_sizings_8():
    width, xgap, xfontsize, minor_ticks, init_margin_offset_l = _get_barchart_sizings('x_title', 30, 40, 1800)
    assert width > 1200 and xgap < 25 and xfontsize >= 8 and minor_ticks == 'true' and init_margin_offset_l == 35
