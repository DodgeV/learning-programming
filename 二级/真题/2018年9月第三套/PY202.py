# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换


##import turtle
##for i in range(4):
##    turtle.fd(100)
##    _________(-100)
##    _________((i+1)*90)


######################答案#####################################
txt = input("请输入类型序列：")
ls = txt.split()
d = {}
for word in ls:
    d[word] = d.get(word,0) + 1
    ls = list(d.items())
ls.sort(key= lambda x:x[1] , reverse = True ) #按照数量排序
for k in ls :
    print("{}:{}".format(k[0],k[1])) 
