 # r e f e r e n c e ： h t t p s : / / b l o g . c s d n . n e t / w e i x i n _ 4 4 4 0 9 0 7 5 / a r t i c l e / d e t a i l s / 8 8 0 8 0 0 9 1 
import globalvar as gl #Package for global var reference：https://www.jb51.net/article/130193.htm#
import os.path
def readOld():
    lrcxPath=gl.get_value('lrcxPath')
    oldLrcx=open(lrcxPath,"r",encoding="utf-8")
    lrcxTmp=os.path.dirname(lrcxPath)+"/lrcxTmp.txt"
    gl.set_value('lrcxTmp',lrcxTmp)
    newLrcx=open(lrcxTmp,"w",encoding="utf-8")
    flag=0
    for line in oldLrcx : #Reading file line by line, the type of line is str 
        flag=0
        if ("offset:" in line) or ("length:" in line) or ("ti:" in line) or ("al:" in line) or ("ar:" in line) or ("[tt]" in line) or ("by:" in line) or ("id:" in line) or ("hash:" in line) or ("[tr:zh-Hans]" in line) or ("sign:" in line):
            continue
        else:
            flag=1
        if flag==1: #Delete the specific content of str reference：https://www.cnblogs.com/zhouzhiyao/p/11498907.html
            lineTmp=line
            lineTmp=list(lineTmp)
            for i in range(11): #Delete the first 11 useless str(which is old time axis) 
                lineTmp.pop(0)
            lineTmp=''.join(lineTmp)
            newLrcx.write(lineTmp)
    oldLrcx.close()
    newLrcx.close()
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    print("The tempt lyric file has been created ")
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
