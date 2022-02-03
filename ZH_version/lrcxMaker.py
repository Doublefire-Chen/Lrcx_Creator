#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import globalvar as gl #全局变量管理库
import os
from pydub import AudioSegment #播放音乐库
'''
创建lrcx的主体框架
'''
def lrcxMaker():
    artist=gl.get_value('artist')
    ti=gl.get_value('musicName')
    lrcxPath=gl.get_value('lrcxPath')
    lrcxPath=lrcxPath+"/"+ti+' '+"-"+" "+artist+".lrcx"
    gl.set_value("lrcxPath",lrcxPath)
    file=open(lrcxPath,'w') #w是清空文件并写入新内容
    #写入length
    musicPath = gl.get_value('musicPath')
    musicFormat = gl.get_value('musicFormat')
    sound = AudioSegment.from_file(musicPath, musicFormat)
    musicTime = round(sound.duration_seconds, 3)
    length=musicTime
    length=str(round(length))
    lrcxPath = gl.get_value('lrcxPath')
    length="[length:"+length+"]"+"\n"
    file.write(length)
    #写入ar
    ar="[ar:"+artist+"]\n"
    file.write(ar)
    #写入offset (默认值：0)
    file.write("[offset:0]\n")
    #写入total
    total=str(round(musicTime)*1000) #最好改为最后的打轴时间
    total="[total:"+total+"]\n"
    file.write(total)
    #写入歌曲名
    ti=gl.get_value('musicName')
    ti="[ti:"+ti+"]\n"
    file.write(ti)
    #写入by
    by=gl.get_value('maker')
    by="[by:"+by+"]\n"
    file.write(by)
    file.close()