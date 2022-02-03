#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import globalvar as gl #全局变量管理库
import os
#实现回车换行，而不是结束 参考：https://blog.csdn.net/weixin_39193977/article/details/116521160
def rawInput():
    lrcxPath = gl.get_value('lrcxPath')
    lrcxTmp = os.path.dirname(lrcxPath) + "/lrcxTmp.txt"
    gl.set_value('lrcxTmp', lrcxTmp)
    tmpLrcx = open(lrcxTmp, "w", encoding="utf-8")
    endstr="" #重新定义结束符
    for line in iter(input,endstr):#每行接收的东西 用了iter的哨兵模式
        tmpLrcx.write(line+"\n")
    tmpLrcx.close()
    print("已生成临时歌词文件")