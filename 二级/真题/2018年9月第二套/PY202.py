# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换

names = input("请输入各个同学行业名称，行业名称之间用空格间隙（回车结束输入）")
...
d = {}
...
ls = list(d.items())
ls.sort(key = lambda x:x[1], reverse =True) # 按照数量排序
for k in ls:
    print("{}:{}".format())


###############答案##################################

    
##names = input("请输入各个同学行业名称，行业名称之间用空格间隙（回车结束输入）")
##ls = names.split()
##d = {}
##for word in ls :
##    d[word] = d.get(word,0) + 1
##ls = list(d.items())
##ls.sort(key = lambda x:x[1], reverse =True) # 按照数量排序
##for k in ls:
##    print("{}:{}".format(k[0],k[1]))
