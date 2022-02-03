#!/usr/bin/python env
#-*- coding:utf-8 -*-
import os
import sys
import globalvar as gl #全局变量管理库 参考：https://www.jb51.net/article/130193.htm#
import time #计时库 高精度计时功能实现的参考：https://zhuanlan.zhihu.com/p/110005305
from playMusic import playMusic #播放音乐函数
from lrcxMaker import lrcxMaker #创建初始lrcx文件
from readOld import readOld
from window import window
from rawInput import rawInput
mode=0
print("*" * 50) #打印分割线
print("请选择制作模式")
print("0、在已有lrcx歌词基础上打逐字滚动时间轴（默认）")
print("1、从无到有创造新的lrcx逐字滚动歌词文件")
mode=input()
gl.set_value('mode',mode)
print("*" * 50) #打印分割线
if mode=="1":
    print("输入您的音乐路径(精确到文件)，将文件直接拖入终端即可\n示例：/Users/Doublefire.Chen/Downloads/Against The Current - See You Again.flac")
    musicPath = input()
    musicPath = musicPath.strip()  # 过滤掉字符首尾的空格' '和换行`\n`
    musicPath = musicPath.replace('\\', '')  # 过滤掉带有空格音乐文件的'\\'
    gl.set_value('musicPath', musicPath)
    musicFormat = os.path.splitext(musicPath)[-1][1:]  # 获取音乐文件的格式
    gl.set_value('musicFormat', musicFormat)
    print("*" * 50)  # 打印分割线
    print("请输入新lrcx文件的存放路径（将文件夹直接拖入终端即可）\n示例：/Users/Doublefire.Chen/Music/LyricsX")
    lrcxPath = input()
    lrcxPath = lrcxPath.strip()  # 过滤掉字符首尾的空格' '和换行`\n`
    lrcxPath = lrcxPath.replace('\\', '')  # 过滤掉带有空格音乐文件的'\\'
    gl.set_value('lrcxPath', lrcxPath)
    print("*" * 50)  # 打印分割线
    print("请输入歌手名")
    artist = input()
    gl.set_value('artist', artist)
    print("*" * 50)  # 打印分割线
    print("请输入歌曲名")
    musicName = input()
    gl.set_value('musicName', musicName)
    print("*" * 50)  # 打印分割线
    print("您作为歌词的创造者，也留下芳名吧")
    maker = input()
    gl.set_value('maker', maker)
    lrcxMaker()
    print("*" * 50)  # 打印分割线
    print("输入您的歌词")
    print("例如：")
    print("Loving him is like driving a new Maserati down a dead-end street\nFaster than the wind, passionate as sin, ending so suddenly\nLoving him is like trying to change your mind\nOnce you're already flying through the free fall\nLike the colors in autumn, so bright just before they lose it all\nLosing him was blue like I'd never known\n······\n\n")
    print("(按回车键1次换行，按回车键2次提交输入)")
    print("*" * 50)  # 打印分割线
    rawInput()
else:
    print("请输入您的原歌词文件路径（将lrcx歌词文件拖进终端即可）\n示例：/Users/Doublefire.Chen/Music/LyricsX/Red - Against The Current Against The Current.lrcx ")
    lrcxPath=input()
    lrcxPath=lrcxPath.strip() #过滤掉字符首尾的空格' '和换行`\n`
    lrcxPath=lrcxPath.replace('\\','') #过滤掉带有空格音乐文件的'\'
    gl.set_value('lrcxPath',lrcxPath)
    readOld()
    print("输入您的音乐路径(精确到文件)，将文件直接拖入终端即可\n示例：/Users/Doublefire.Chen/Downloads/Against The Current - See You Again.flac")
    musicPath = input()
    musicPath = musicPath.strip()  # 过滤掉字符首尾的空格' '和换行`\n`
    musicPath = musicPath.replace('\\', '')  # 过滤掉带有空格音乐文件的'\\'
    gl.set_value('musicPath', musicPath)
    musicFormat = os.path.splitext(musicPath)[-1][1:]  # 获取音乐文件的格式
    gl.set_value('musicFormat', musicFormat)
    print("*" * 50)  # 打印分割线
    print("请输入新lrcx文件的存放路径（将文件夹直接拖入终端即可）\n示例：/Users/Doublefire.Chen/Music/LyricsX")
    lrcxPath = input()
    lrcxPath = lrcxPath.strip()  # 过滤掉字符首尾的空格' '和换行`\n`
    lrcxPath = lrcxPath.replace('\\', '')  # 过滤掉带有空格音乐文件的'\\'
    gl.set_value('lrcxPath', lrcxPath)
    print("*" * 50)  # 打印分割线
    print("请输入歌手名")
    artist = input()
    gl.set_value('artist', artist)
    print("*" * 50)  # 打印分割线
    print("请输入歌曲名")
    musicName = input()
    gl.set_value('musicName', musicName)
    print("*" * 50)  # 打印分割线
    print("您作为歌词的创造者，也留下芳名吧")
    maker = input()
    gl.set_value('maker', maker)
    lrcxMaker()
window()