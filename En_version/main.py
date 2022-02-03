#!/usr/bin/python env
#-*- coding:utf-8 -*-
import os
import sys
import globalvar as gl #The package for global var reference：https://www.jb51.net/article/130193.htm#
import time #The package for precise timing reference：https://zhuanlan.zhihu.com/p/110005305
from playMusic import playMusic #The package for music playing 
from lrcxMaker import lrcxMaker #Creat original lrcx file 
from readOld import readOld
from window import window
from rawInput import rawInput
mode=0
print("*" * 50) #Print split line
print("*" * 50) #Print split line
print("Please choose mode ")
print("0.Create new lrcx file based on old lrcx file(default) ")
print("1.Create new lrcx file from nothing ")
mode=input()
gl.set_value('mode',mode)
print("*" * 50) #Print split line
print("*" * 50) #Print split line
if mode=="1":
    print("Please input your music path(exactly your song file), you can just drag the music file to the terminal\neg:/Users/Doublefire.Chen/Downloads/Against The Current - See You Again.flac ")
    musicPath = input()
    musicPath = musicPath.strip()  #The filter for space' 'and line feed'\n' 
    musicPath = musicPath.replace('\\', '')  #The filter for '\' 
    gl.set_value('musicPath', musicPath)
    musicFormat = os.path.splitext(musicPath)[-1][1:]  #Obtain the format of music file 
    gl.set_value('musicFormat', musicFormat)
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    print("Please input thedeposit path for new lrcx file(you can just drag the folder to the terminal)\neg:/Users/Doublefire.Chen/Music/LyricsX ")
    lrcxPath = input()
    lrcxPath = lrcxPath.strip()  #The filter for space' 'and line feed'\n' 
    lrcxPath = lrcxPath.replace('\\', '')  #The filter for '\'  
    gl.set_value('lrcxPath', lrcxPath)
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    print("Please input the name of the artist ")
    artist = input()
    gl.set_value('artist', artist)
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    print("Please input the name of the song ")
    musicName = input()
    gl.set_value('musicName', musicName)
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    print("Please input your name as a creator ")
    maker = input()
    gl.set_value('maker', maker)
    lrcxMaker()
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    print("Please input your lyrics ")
    print("For example: ")
    print("Loving him is like driving a new Maserati down a dead-end street\nFaster than the wind, passionate as sin, ending so suddenly\nLoving him is like trying to change your mind\nOnce you 're already flying through the free fall\nLike the colors in autumn, so bright just before they lose it all\nLosing him was blue like I'd never known\n······\n\n")
    print("(press enter key one time means line feed, two times mean the end of input) ")
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    rawInput()
else:
    print("Please input your original lrcx file path(you can just drag the lrcx file to the termianl)\neg:/Users/Doublefire.Chen/Music/LyricsX/Red - Against The Current Against The Current.lrcx ")
    lrcxPath=input()
    lrcxPath=lrcxPath.strip() #The filter for space' 'and line feed'\n' 
    lrcxPath=lrcxPath.replace('\\','') #The filter for '\'   
    gl.set_value('lrcxPath',lrcxPath)
    readOld()
    print("Please input your music path(exactly your song file), you can just drag the music file to the terminal\neg:/Users/Doublefire.Chen/Downloads/Against The Current - See You Again.flac ")
    musicPath = input()
    musicPath = musicPath.strip()  #The filter for space' 'and line feed'\n' 
    musicPath = musicPath.replace('\\', '')  #The filter for '\'   
    gl.set_value('musicPath', musicPath)
    musicFormat = os.path.splitext(musicPath)[-1][1:]  #Obtain the format of music file 
    gl.set_value('musicFormat', musicFormat)
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    print("Please input the deposit path for new lrcx file(you can just drag the folder to the terminal)\neg:/Users/Doublefire.Chen/Music/LyricsX ")
    lrcxPath = input()
    lrcxPath = lrcxPath.strip()  #The filter for space' 'and line feed'\n' 
    lrcxPath = lrcxPath.replace('\\', '')  #The filter for '\' 
    gl.set_value('lrcxPath', lrcxPath)
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    print("Please input the name of the artist ")
    artist = input()
    gl.set_value('artist', artist)
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    print("Please input the name of the song ")
    musicName = input()
    gl.set_value('musicName', musicName)
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    print("Please input your name as a creator ")
    maker = input()
    gl.set_value('maker', maker)
    lrcxMaker()
window()