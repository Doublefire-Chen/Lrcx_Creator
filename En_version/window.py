#The lyric window reference：https://www.cnblogs.com/wwf828/p/7418181.html
import time #The package for precise timing reference：https://zhuanlan.zhihu.com/p/110005305
def window():
    print("*" * 50)  # Print split line
    print("*" * 50)  # Print split line
    print("Create interact window ")
    import tkinter as tk
    import globalvar as gl  #The package for global var reference：https://www.jb51.net/article/130193.htm#
    import os.path
    from threading import Thread  #Use threading function 
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
                    window.destroy()  #Close window reference：https://blog.csdn.net/weixin_39989980/article/details/110628605
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
                    window.destroy()  #Close window reference：https://blog.csdn.net/weixin_39989980/article/details/110628605
                    break
                wordcount = 0
                counTemp = 0
            if startFlag==1:
                lyric.tag_add(symb, lineTemp, count)
                lyric.tag_config(symb, foreground='blue')  # reference：https://blog.csdn.net/nkd50000/article/details/77103700
                lyric.update()
                symb = str(linecount) + str(wordcount)
            event.char = "q"
    def Zh_or_En(strs):     #Determine whether Chinese or English reference：https://blog.csdn.net/lwdfzr/article/details/105402804
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
    def cut(obj, sec):  # reference：https://blog.csdn.net/qq_26373925/article/details/101135611
        return [obj[i:i + sec] for i in range(0, len(obj), sec)]
    def timeTrans(time):
        min=0
        while time>60:
            time=time-60
            min=min+1
        min=str(min).rjust(2,'0')  #The time format transform reference：https://blog.csdn.net/weixin_44208042/article/details/93328869
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
    #This is content in window 
    l = tk.Label(window,
                text='Please press space key to add time axis(in every line you need to press space key one time which means start, \nwhen one unit has already been songed, press space key one time\n The English lyric is splted by space, and Chinese lyric is split by word by word\nif English and Chinese both exit, the sentence will be splited by space\nThe auto pagedown is not available, you need to do it by your hands\nThe music will play after 5 seconds',  #The words in label 
                bg='yellow',  #The back color 
                font=('system', 16),  #The font and font sizes 
                width=150, height=6)  #The length an width of label 
    l.pack()  #Make window position fixed 
    lyric = tk.Text(window,
                    width=150,
                    font=('system', 36),
                    fg=color)
    lyric.pack()
    linecount = 0
    newLrcx = open(lrcxTmp, "r", encoding="utf-8")
    lineTotal = len(newLrcx.readlines())-1  #The last line of txt will not count, which means the line count is exactly the line with words 
    array = [[0 for i in range(100)] for j in range(100)]  #Create 2 dimension array reference：https://zhuanlan.zhihu.com/p/88197389
    arrayTime = [[0 for i in range(100)] for j in range(100)]  #Create 2 dimension array reference：https://zhuanlan.zhihu.com/p/88197389
    lrcxTmp=gl.get_value('lrcxTmp')
    newLrcx = open(lrcxTmp, "r", encoding="utf-8")
    for line in newLrcx:  #Reading file line by line the type of line is str 
        if Zh_or_En(line) == "En":
            lyric.insert("insert", line)  #"insert" means insert in cursor position 
            array[linecount] = line.split()
            linecount = linecount + 1
            Ch_En_space = 1
        else:
            lyric.insert("insert", line)
            line = line.strip()  #Filter for space ' ' and line feed '\n' in str first and tail 
            array[linecount] = cut(line, 1)
            linecount = linecount + 1
            Ch_En_space = 0
    newLrcx.close()
    lyric.config(state='disabled')  # reference：https://zhidao.baidu.com/question/1959930961650330100.html
    linecount=0
    def bind():
        bind=window.bind('<Key>', color_change)
    t1 = Thread(target=bind)
    t2 = Thread(target=playMusic) #Remember do not add(), or the function will run directly reference：https://ask.csdn.net/questions/364905
    t1.start()  #Start run thread t1 
    t2.start()  #Start run thread t2 
    window.mainloop()
    lrcxPath=gl.get_value("lrcxPath")
    tmpLrcx=open(lrcxTmp,"r",encoding="utf-8")
    lrcx = open(lrcxPath, 'a',encoding="utf-8")  #Start write in the tail of file(if existed) 
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
    print("The tempt lyric file has been deleted ")