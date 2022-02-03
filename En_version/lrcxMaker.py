#!/usr/bin/python 
# -*- coding: utf-8 -*- 
import sys
import globalvar as gl #The mode for global var 
import os
from pydub import AudioSegment #The package for music playing 
'''
创建lrcx的主体框架
'''
def lrcxMaker():
    artist=gl.get_value('artist')
    ti=gl.get_value('musicName')
    lrcxPath=gl.get_value('lrcxPath')
    lrcxPath=lrcxPath+"/"+ti+' '+"-"+" "+artist+".lrcx"
    gl.set_value("lrcxPath",lrcxPath)
    file=open(lrcxPath,'w') #w means clean old file and write new contents 
    #write length 
    musicPath = gl.get_value('musicPath')
    musicFormat = gl.get_value('musicFormat')
    sound = AudioSegment.from_file(musicPath, musicFormat)
    musicTime = round(sound.duration_seconds, 3)
    length=musicTime
    length=str(round(length))
    lrcxPath = gl.get_value('lrcxPath')
    length="[length:"+length+"]"+"\n"
    file.write(length)
    #write ar 
    ar="[ar:"+artist+"]\n"
    file.write(ar)
    #write offset (default:0) 
    file.write("[offset:0]\n")
    #write total 
    total=str(round(musicTime)*1000) #It is better to change it as the last time asix 
    total="[total:"+total+"]\n"
    file.write(total)
    #Write the name of the song 
    ti=gl.get_value('musicName')
    ti="[ti:"+ti+"]\n"
    file.write(ti)
    #Write by 
    by=gl.get_value('maker')
    by="[by:"+by+"]\n"
    file.write(by)
    file.close()