from funzione import tmux_format
from datetime import timedelta

def test_tmux_format_1():
    assert tmux_format(True, timedelta(days=0, seconds=0)) == "#[reverse,fg=colour4,bg=white]  KW  "

def test_tmux_format_2():
    assert tmux_format(True, timedelta(days=1, seconds=0)) == "#[reverse,fg=colour4,bg=white]  KW  1 min  "

def test_tmux_format_3():
    assert tmux_format(True, timedelta(days=-1, seconds=0)) == "#[noreverse,fg=black,bg=yellow]  HB  "

def test_tmux_format_4():
    assert tmux_format(False, timedelta(days=0, seconds=0)) == "#[noreverse,fg=black,bg=green]  EB  "

def test_tmux_format_5():
    assert tmux_format(False, timedelta(days=1, seconds=0)) == "#[noreverse,fg=black,bg=green]  EB  1 min  "

def test_tmux_format_6():
    assert tmux_format(False, timedelta(days=-1, seconds=0)) == "#[reverse,fg=colour1,bg=white]  GW  "

def test_tmux_format_7():
    assert tmux_format(True, timedelta(days=0, seconds=60)) == "#[reverse,fg=colour4,bg=white]  KW: 2 mins  "

def test_tmux_format_8():
    assert tmux_format(False, timedelta(days=0, seconds=60)) == "#[noreverse,fg=black,bg=green]  EB: 2 mins  "
