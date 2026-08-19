import pytest
from datetime import timedelta

def tmux_format(working, x):
    if working and x.days >= 0:
        message = "KW"
        r = "reverse"
        fg = "colour4"
        bg = "white"
    elif working and x.days < 0:
        message = "HB"
        r = "noreverse"
        fg = "black"
        bg = "yellow"
    elif not working and x.days >= 0:
        message = "EB"
        r = "noreverse"
        fg = "black"
        bg = "green"
    elif not working and x.days < 0:
        message = "GW"
        r = "reverse"
        fg = "colour1"
        bg = "white"

    s = "#[%s,fg=%s,bg=%s]  %s" % (r, fg, bg, message)

    if x.days >= 0:
        n = x.seconds / 60 + 1
        if n == 1:
            s += ": %d min" % n
        else:
            s += ": %d mins" % n

    return s + "  "

def test_tmux_format_1():
    assert tmux_format(True, timedelta(days=0)) == "#[colour4,fg=white] KW"
    assert tmux_format(False, timedelta(days=-1)) == "#[black,fg=black,bg=yellow] HB"

def test_tmux_format_2():
    assert tmux_format(True, timedelta(days=10)) == "#[reverse,fg=colour4,bg=white]  20 min"
    assert tmux_format(False, timedelta(days=-5)) == "#[noreverse,fg=black,bg=yellow] GW"

def test_tmux_format_3():
    assert tmux_format(True, timedelta(days=30)) == "#[colour1,fg=colour4,bg=white]  30 mins"
    assert tmux_format(False, timedelta(days=-20)) == "#[noreverse,fg=black,bg=green] EB"

def test_tmux_format_4():
    with pytest.raises(ValueError):
        tmux_format(True, timedelta(days=0))

def test_tmux_format_5():
    assert tmux_format(False, timedelta(days=1)) == "KW"
