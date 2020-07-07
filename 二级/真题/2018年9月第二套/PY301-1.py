# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换


...
for line in ______:
...
    fo.write('{},{},{},{}\n'.format(______))
...

#############答案##############################
##fi = open("sensor.txt",'r',encoding='utf-8')   #如果运行后出现了Unicode错误，则添加上encoding='utf-8'
##fo = open("earpa001.txt","w")
##for line in fi:
##    ls = line.strip("\n").split(",")   #strip("\n")除去行尾的换行符，split(",")将每行的逗号进行分隔，可以通过print(ls)查看一下该内容是什么样的。
##    if "earpa001" in ls[1]:
##        fo.write('{},{},{},{}\n'.format(ls[0],ls[1],ls[2],ls[3]))
##fi.close()
##fo.close()
