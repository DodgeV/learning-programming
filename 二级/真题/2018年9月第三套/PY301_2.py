# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换



fi = open("论语-原文.txt", ______)
fo = open("论语-提纯原文.txt", ______)
...
for line in fi:
...
    line=line.replace(______)
...


######################答案#####################################
##fi = open("论语-原文.txt", "r")
##fo = open( "论语-提纯原文.txt" , "w")
##for line in fi: #逐行遍历
##    for i in range (1,23):  #对产生 1 到 22 数字
##        line = line.replace("({})".format(i),"") #构造（ i ）并替换
##    fo.write(line)
##fi.close()
##fo.close()
