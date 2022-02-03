#参考：https://blog.csdn.net/weixin_44409075/article/details/88080091
import globalvar as gl #全局变量管理库 参考：https://www.jb51.net/article/130193.htm#
import os.path
def readOld():
    lrcxPath=gl.get_value('lrcxPath')
    oldLrcx=open(lrcxPath,"r",encoding="utf-8")
    lrcxTmp=os.path.dirname(lrcxPath)+"/lrcxTmp.txt"
    gl.set_value('lrcxTmp',lrcxTmp)
    newLrcx=open(lrcxTmp,"w",encoding="utf-8")
    flag=0
    for line in oldLrcx : #按行读入文件，此时line的type是str
        flag=0
        if ("offset:" in line) or ("length:" in line) or ("ti:" in line) or ("al:" in line) or ("ar:" in line) or ("[tt]" in line) or ("by:" in line) or ("id:" in line) or ("hash:" in line) or ("[tr:zh-Hans]" in line) or ("sign:" in line):
            continue
        else:
            flag=1
        if flag==1: #删除字符串的特定内容 参考：https://www.cnblogs.com/zhouzhiyao/p/11498907.html
            lineTmp=line
            lineTmp=list(lineTmp)
            for i in range(11): #删去了前面11个没用的字符（原来的时间轴）
                lineTmp.pop(0)
            lineTmp=''.join(lineTmp)
            newLrcx.write(lineTmp)
    oldLrcx.close()
    newLrcx.close()
    print("*" * 50)  # 打印分割线
    print("已生成临时歌词文件")
    print("*" * 50)  # 打印分割线
