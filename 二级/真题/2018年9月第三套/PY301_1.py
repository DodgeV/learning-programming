# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换

fi = open("论语.txt", ______)
fo = open("论语-原文.txt", ______)
...
for line in fi:
...
    line = line.strip(" \n")
...


######################答案#####################################
##fi = open ('论语.txt',"r")
##fo = open ( "论语-原文.txt", "w" )
##wflag = False
##for line in fi :
##    if "【" in line:
##        wflag = False
##    if "【原文】" in line :
##        wflag = True
##        continue
##    if wflag == True :
##        line = line.strip(" ")
##        if line.count('\n') != len(line):
##            fo.write(line)
##fi.close()
##fo.close() 
