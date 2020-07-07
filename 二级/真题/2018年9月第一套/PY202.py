#注：下面的代码中请在...处使用一行或多行代码替换
#   请在____处使用一行代码替换
#   本题15分

data = input() #姓名  年龄  性别
...
while data:
    ...
    data = input()
...
print("平均年龄是{:.2f} 男性人数是{}".format(_____))




#####################参考答案##################################
#请将下面的代码取消注释即可

##data = input() #姓名  年龄  性别
##info = {}    #定义一个字典
##i  = 0
##man_num = 0
##age_total = 0
##while data:
##    info[i] = data.split(" ")   #将输入的一行信息存储在字典info中，键为数字i，值为 输入的信息通过split转换为列表，如果看不懂，可以通过print(data.split(" "))来查看具体形式
##    i = i+1
##    age_total += int(data.split(" ")[2])  #统计年龄总和
##    if data.split(" ")[1] == "男": #这行和下面一行是统计为男性的个数
##        man_num = man_num + 1   
##    data = input()
##age_aver = age_total/i   #计算平均年龄
##print("平均年龄是{:.2f} 男性人数是{}".format(age_aver,man_num))
