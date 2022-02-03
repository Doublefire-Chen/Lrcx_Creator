#!/usr/bin/python 
# -*- coding: utf-8 -*- 
import sys
import globalvar as gl #Package for global var 
import os
#Make enter key become line feed instead of end reference：https://blog.csdn.net/weixin_39193977/article/details/116521160
def rawInput():
    lrcxPath = gl.get_value('lrcxPath')
    lrcxTmp = os.path.dirname(lrcxPath) + "/lrcxTmp.txt"
    gl.set_value('lrcxTmp', lrcxTmp)
    tmpLrcx = open(lrcxTmp, "w", encoding="utf-8")
    endstr="" #Reassign end str 
    for line in iter(input,endstr):#str in each line. The guard mode of iter is used 
        tmpLrcx.write(line+"\n")
    tmpLrcx.close()
    print("The tempt lyric file has been created ")