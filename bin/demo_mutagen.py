#!/usr/bin/env python3
import os
from pathlib import Path

VJOT_RAW=Path(os.environ['VJOT_RAW'])



allfiles = list(VJOT_RAW.glob('*.mp3'))


from mutagen.mp3 import MP3

def mutagen_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None
acc=[]
for path in allfiles:
    length = mutagen_length(path)
    length = length and int(length)
    acc.append( (length, path) )
    print( length, path)
exit()
acc.sort
for xx in acc[-10:]:
    print(xx)
    #print(length,path)
    #print("duration sec: " + str(length))
    #print("duration min: " + str(int(length/60)) + ':' + str(int(length%60)))

