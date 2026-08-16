from funzione import tmux_format
import datetime

def test_tmux_format_1():
    working = True
    x = datetime.timedelta(days=0, seconds=30)
    assert tmux_format(working, x) == "#[noreverse,fg=colour4,bg=white]  KW: 2 mins  "

def test_tmux_format_2():
    working = False
    x = datetime.timedelta(days=1, seconds=0)
    assert tmux_format(working, x) == "#[reverse,fg=colour1,bg=white]  GW  "

def test_tmux_format_3():
    working = True
    x = datetime.timedelta(days=-1, seconds=30)
    assert tmux_format(working, x) == "#[noreverse,fg=black,bg=yellow]  HB: 2 mins  "

def test_tmux_format_4():
    working = False
    x = datetime.timedelta(days=-1, seconds=0)
    assert tmux_format(working, x) == "#[reverse,fg=colour4,bg=white]  GW  "

def test_tmux_format_5():
    working = True
    x = datetime.timedelta(seconds=30)
    assert tmux_format(working, x) == "#[noreverse,fg=colour4,bg=white]  KW: 1 min  "

def test_tmux_format_6():
    working = False
    x = datetime.timedelta(days=0, seconds=0)
    assert tmux_format(working, x) == "#[noreverse,fg=black,bg=green]  EB  "
