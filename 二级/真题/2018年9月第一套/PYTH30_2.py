##  问题2：统计命运.txt 中字符个数，包含中文符号和英文符号，不包含换行空格；将最高频率的前10个字符及频率输出
##  例如：
##  理斯卫...
##注意：每个字符输出在同一行，不换行。

...
d = {}
...
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True) # 此行可以按照词频由高到低排序
...



###################答案####################################################
##fate = open('命运-网络版.txt','r',encoding = 'utf-8')
##lines = fate.read()
##fate.close()
##fuhao = ['《','》','-',' ','。','？','（','）','，','：','"','、','！','\n','\u3000']   #这里\u3000代表全角空格，在考试的时候没有这种问题存在。在题录中的命运-网络版.txt我呢本中存在全角空格
##d={}       
##for word in lines:
##    if word in fuhao:
##        continue
##    else:
##        d[word] = d.get(word,0) + 1    #相同字符出现则加1
##ls = list(d.items())              #可以通过print(ls)尝试打印出ls的内容是什么样子。
##ls.sort(key = lambda x:x[1],reverse = True)#本行代码题目已经给出的，将ls按照统计数量进行从大大小排序，当reverse=False时：为正向排序；当reverse=True时：为反向排序。
##for i in range(10):
##    print(ls[i][0],end= '')   #将字符输出，不包含回车符，字符无间隙
