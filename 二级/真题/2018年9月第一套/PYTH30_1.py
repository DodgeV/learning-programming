##  问题1：统计命运.txt 中中文字符个数，将最高频率的是字符及频率输出
##  例如：
##  理:224
# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换

...
d = {}
...
ls = list(d.items())
ls.sort(key = lambda x:x[1],reverse = True)
print("{}:{}".format(______))

######################答案#####################################
##fate = open('命运-网络版.txt','r',encoding = 'utf-8')
##lines = fate.read()
##fuhao = ['《','》','-',' ','。','？','（','）','，','：','"','、','！','\n','\u3000']  #这里\u3000代表全角空格，在考试中没有这种问题存在。在题录中的命运-网络版.txt我呢本中存在全角空格
##d={}       #定义一个空字典，用于存储相同字符出现的个数
##for word in lines:
##    if word in fuhao:  #除去符号
##        continue
##    else:
##        d[word] = d.get(word,0) + 1   #相同字符出现则加1
##fate.close()
##ls = list(d.items())   #可以通过print(ls)尝试打印出ls的内容是什么样子。
##ls.sort(key = lambda x:x[1],reverse = True)#本行代码题目已经给出的，将ls按照统计数量进行从大大小排序，当reverse=False时：为正向排序；当reverse=True时：为反向排序。
##print('{}:{}'.format(ls[0][0],ls[0][1]))
