# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

...
ls = []
...
      print("{}({})的生日是{}月{}日至{}月{}日之间".format(______))
...
      if flag == False:
            print("输入星座序号有误！")
...


######################答案###################################

##fo = open("PY301-Sunsign.csv" ,"r")
##ls = []
##for line in fo :
##    line = line.replace("\n","")   #取消每一行的换行符
##    ls.append(line.split(","))
##fo.close()
##while True :
##    Inputstr = input("请输入1-12的整数：")
##    txt = Inputstr.split(" ")
##    for i in txt :
##        flag = False
##        for line in ls :
##            if i == line[0] :
##                print("{}({})的生日是{}月{}日至{}月{}日之间".format((line[1]),(line[4]),line[2][:-2],line[2][-2:],line[3][:-2],line[3][-2:]))
##                flag = True
##        if flag == False:
##            print("输入星座序号有误")
