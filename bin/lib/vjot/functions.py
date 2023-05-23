#!/usr/bin/env python3

import os
from pathlib import Path
from collections import defaultdict
from vjot.constants import ROOT

def select(prefix):
    fn = lambda vjot : stamp4vjot(vjot).startswith(prefix)
    return sorted( list( filter( fn, vjots() ) ) )

def walk(path):
    yield path
    if path.is_dir():
        for child in path.glob('*'):
            yield from walk(child)

def stamp4vjot(vjot):
    assert is_vjot(vjot)
    stamp=vjot.name.split('.')[0]
    assert is_stamp(stamp)
    return stamp

def is_stamp(text): return len(text)==15 and text[8] in 'tT'
def is_vjot(path): return path.name.upper().endswith('.MP3')
def vjots(): return filter(is_vjot, walk(ROOT))

def validate():
    for path in vjots():
        assert path.name.endswith( '.ws852.mp3' )
        assert stamp4vjot(vjot)

def vjot4stamp(stamp):
    for vjot in vjots():
        if stamp4vjot(vjot) == stamp:
            return vjot

def audio4vjot(vjot):
    os.system( f"bh.beep-play {vjot}")
