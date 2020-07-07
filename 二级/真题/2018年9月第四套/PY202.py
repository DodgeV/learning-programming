# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#



##import turtle as _____
##for i in range(______) :
##    t.seth(i*120)
##    t.fd(_______)

##########################答案######################################

data = input() #课程名考分
d = {}
while data :
    data = data.split()
    d[data[0]] = data[1]
    data = input()
ls = list(d.items())
ls.sort(key = lambda x:x[1], reverse = True )
maxn,maxl = ls[0]
minn,minl = ls[len(ls)- 1]
avg = 0
for i in d.values() :
    avg = avg + int(i)
avg = avg/len(ls)
print("最高分课程是{} {}，最低分课程是{} {}，平均分是{:.2f}".format(maxn,maxl,minn,minl,avg)) 





