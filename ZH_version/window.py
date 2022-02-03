#歌词窗口的实现 参考：https://www.cnblogs.com/wwf828/p/7418181.html
import time #计时库 高精度计时功能实现的参考：https://zhuanlan.zhihu.com/p/110005305
def window():
    print("*" * 50)  # 打印分割线
    print("生成交互窗口")
    import tkinter as tk
    import globalvar as gl  # 全局变量管理库 参考：https://www.jb51.net/article/130193.htm#
    import os.path
    from threading import Thread  # 导入线程函数
    from playMusic import playMusic
    def color_change(event):
        global count,counTemp,linecount,wordcount,symb,startTime,startFlag
        while event.char == ' ':
            if linecount+wordcount+startFlag==0:
                startTime = time.perf_counter()
                startFlag=1
                event.char="q"
                continue
            arrayTime[linecount][wordcount]=time.perf_counter()
            lineTemp=linecount+1
            lineTemp = ("%.1f" % lineTemp)
            if wordcount < len(array[linecount]):
                if linecount > lineTotal:
                    window.destroy()  # 关闭窗口 参考：https://blog.csdn.net/weixin_39989980/article/details/110628605
                    break
                counTemp = counTemp + len(array[linecount][wordcount]) + Ch_En_space
                if counTemp < 10:
                    count = linecount + counTemp / 10+1
                    count = ("%.1f" % count)
                    wordcount = wordcount + 1
                elif 10 <= counTemp < 100:
                    count = linecount + counTemp / 100+1
                    count = ("%.2f" % count)
                    wordcount = wordcount + 1
                elif 100 <= counTemp < 1000:
                    count = linecount + counTemp / 1000+1
                    count = ("%.3f" % count)
                    wordcount = wordcount + 1
            else:
                linecount = linecount + 1
                if linecount > lineTotal:
                    window.destroy()  # 关闭窗口 参考：https://blog.csdn.net/weixin_39989980/article/details/110628605
                    break
                wordcount = 0
                counTemp = 0
            if startFlag==1:
                lyric.tag_add(symb, lineTemp, count)
                lyric.tag_config(symb, foreground='blue')  # 参考：https://blog.csdn.net/nkd50000/article/details/77103700
                lyric.update()
                symb = str(linecount) + str(wordcount)
            event.char = "q"
    def Zh_or_En(strs):     # 判断中英文 参考：https://blog.csdn.net/lwdfzr/article/details/105402804
        strs = strs.strip()
        Zhcount = 0
        Encount = 0
        for i in strs:
            if not '\u4e00' <= i <= '\u9fa5':
                Encount = Encount + 1
            else:
                Zhcount = Zhcount + 1
        if Encount > Zhcount:
            return "En"
        else:
            return "Zh"
    def cut(obj, sec):  # 参考：https://blog.csdn.net/qq_26373925/article/details/101135611
        return [obj[i:i + sec] for i in range(0, len(obj), sec)]
    def timeTrans(time):
        min=0
        while time>60:
            time=time-60
            min=min+1
        min=str(min).rjust(2,'0')  #时间格式的转化 参考：https://blog.csdn.net/weixin_44208042/article/details/93328869
        time=round(time,3)
        time=str(time).rjust(2,'0')
        time="["+min+":"+time+"]"
        return time
    global count, symb, counTemp, linecount, wordcount, lineTemp, Ch_En_space, lineTotal, lyric, array,arrayTime,startTime,startFlag
    linecount = 0
    wordcount = 0
    counTemp=0
    color = "black"
    symb="qq"
    startTime=0
    startFlag=0
    lrcxTmp = gl.get_value('lrcxTmp')
    newLrcx = open(lrcxTmp, "r", encoding="utf-8")
    window = tk.Tk()
    window.title('Lrcx_creater')
    window.geometry('1000x1000')
    # 这里是窗口的内容
    l = tk.Label(window,
                text='按空格键打轴（每一行歌词最开始需要按一次空格表示开始唱这句歌词了，唱完一个单位就按一下空格），\n英文是以每个空格为间隔分开成各个单位，中文每个汉字为一个单位，\n同时有中英文仍以每个空格为间隔分开成各个单位\n未设置自动翻页，需要手动向下翻页\n5秒后开始播放音乐',  # 标签的文字
                bg='yellow',  # 背景颜色
                font=('system', 16),  # 字体和字体大小
                width=150, height=6)  # 标签长宽
    l.pack()  # 固定窗口位置
    lyric = tk.Text(window,
                    width=150,
                    font=('system', 36),
                    fg=color)
    lyric.pack()
    linecount = 0
    newLrcx = open(lrcxTmp, "r", encoding="utf-8")
    lineTotal = len(newLrcx.readlines())-1  # txt最后的空行会少算一行，正好是包含文字的行数
    array = [[0 for i in range(100)] for j in range(100)]  # 创建二维数组 参考：https://zhuanlan.zhihu.com/p/88197389
    arrayTime = [[0 for i in range(100)] for j in range(100)]  # 创建二维数组 参考：https://zhuanlan.zhihu.com/p/88197389
    lrcxTmp=gl.get_value('lrcxTmp')
    newLrcx = open(lrcxTmp, "r", encoding="utf-8")
    for line in newLrcx:  # 按行读入文件，此时line的type是str
        if Zh_or_En(line) == "En":
            lyric.insert("insert", line)  # "insert" 索引表示插入光标当前的位置
            array[linecount] = line.split()
            linecount = linecount + 1
            Ch_En_space = 1
        else:
            lyric.insert("insert", line)
            line = line.strip()  # 过滤掉字符串首尾的空格' '和换行`\n`
            array[linecount] = cut(line, 1)
            linecount = linecount + 1
            Ch_En_space = 0
    newLrcx.close()
    lyric.config(state='disabled')  # 参考：https://zhidao.baidu.com/question/1959930961650330100.html
    linecount=0
    def bind():
        bind=window.bind('<Key>', color_change)
    t1 = Thread(target=bind)
    t2 = Thread(target=playMusic) #千万别加括号，否则程序就直接运行了 参考：https://ask.csdn.net/questions/364905
    t1.start()  # 开始运行t1线程
    t2.start()  # 开始运行t2线程
    window.mainloop()
    lrcxPath=gl.get_value("lrcxPath")
    tmpLrcx=open(lrcxTmp,"r",encoding="utf-8")
    lrcx = open(lrcxPath, 'a',encoding="utf-8")  # 打开写入，追加到文件末尾（如果存在）
    writeFlag=0
    linecount=0
    wordcount=0
    albetcount=0
    for line in tmpLrcx:
        if writeFlag==0:
            T0=gl.get_value("T0")
            lrcx.write(timeTrans(arrayTime[0][0]-T0)+line)
            lrcx.write(timeTrans(arrayTime[0][0] - T0)+"[tt]<0,0>")
            while wordcount<=len(array[linecount]):
                if wordcount<len(array[linecount]):
                    albetcount=albetcount+len(array[linecount][wordcount])+1
                    lrcx.write("<"+str(round((arrayTime[linecount][wordcount]-startTime)*1000))+","+str(albetcount)+">")
                    wordcount=wordcount+1
                else:
                    lrcx.write("<"+str(round((arrayTime[linecount][wordcount-1]-startTime)*1000))+">"+"\n")
                    linecount=linecount+1
                    wordcount=0
                    albetcount=0
                    writeFlag=1
                    break
        else:
            if linecount==len(array)-1:
                break
            if "\n" not in line:
                lrcx.write(timeTrans(arrayTime[linecount-1][len(array[linecount-1])]-T0)+line+"\n")
            elif "\n" in line:
                lrcx.write(timeTrans(arrayTime[linecount-1][len(array[linecount-1])]-T0)+line)
            lrcx.write(timeTrans(arrayTime[linecount-1][len(array[linecount-1])]-T0)+"[tt]<0,0>")
            while wordcount <= len(array[linecount]):
                if wordcount<len(array[linecount]):
                    albetcount = albetcount + len(array[linecount][wordcount]) + 1
                    lrcx.write("<" + str(round((arrayTime[linecount][wordcount] - arrayTime[linecount-1][len(array[linecount-1])]) * 1000)) +","+ str(albetcount) + ">")
                    wordcount=wordcount+1
                else:
                    lrcx.write("<" + str(round((arrayTime[linecount][wordcount-1] - arrayTime[linecount-1][len(array[linecount-1])]) * 1000)) + ">"+"\n")
                    linecount = linecount + 1
                    wordcount = 0
                    albetcount = 0
                    break
    tmpLrcx.close()
    lrcx.close()
    os.remove(lrcxTmp)
    print("已删除临时歌词文件")