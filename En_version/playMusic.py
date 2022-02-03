#!/usr/bin/python 
# -*- coding: utf-8 -*- 
import sys
import globalvar as gl #Package for global var 
from pydub import AudioSegment #Package for music playing 
from pydub.playback import play #Package for music playing 
import time
def playMusic():
    print("The song will play after 5 seconds ")
    time.sleep(5)
    print("Start playing song ")
    musicPath=gl.get_value('musicPath')
    musicFormat=gl.get_value('musicFormat')
    sound=AudioSegment.from_file(musicPath, musicFormat)
    #Test by myself:mp3,flac,ape,wav are available, but dff is not available. The package used is FFmpeg, in principle format is available while it is suitable in FFmpeg. You can also test by yourself. 
    T0=time.perf_counter()
    gl.set_value("T0",T0)
    play(sound)
    print("End music playing ")