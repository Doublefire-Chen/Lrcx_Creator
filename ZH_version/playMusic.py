#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import globalvar as gl #全局变量管理库
from pydub import AudioSegment #播放音乐库
from pydub.playback import play #播放音乐库
import time
def playMusic():
    print("音乐将在5秒后播放")
    time.sleep(5)
    print("开始播放音乐")
    musicPath=gl.get_value('musicPath')
    musicFormat=gl.get_value('musicFormat')
    sound=AudioSegment.from_file(musicPath, musicFormat)
    #亲测：支持mp3,flac,ape,wav,不支持dff。用的FFmpeg包，原则上是FFmpeg支持的格式都支持播放。别的文件格式也可以自行测试。
    T0=time.perf_counter()
    gl.set_value("T0",T0)
    play(sound)
    print("音乐播放结束")