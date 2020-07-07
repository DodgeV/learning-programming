##  问题3：统计命运.txt 中字符个数，包含中文符号和英文符号，不包含换行空格；将统计结果写入命运-频率统计.txt中。
##  统计文本格式例如：
##  理:224，斯:120,卫:100

...
d = {}
...
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True) # 此行可以按照词频由高到低排序
...

########################答案########################################
##fate = open('命运-网络版.txt','r',encoding = 'utf-8')
##lines = fate.read()
##fate.close()
##fuhao = [' ','\n','\u3000']  #这里\u3000代表全角空格，在考试的时候没有这种问题存在。在题录中的命运-网络版.txt我呢本中存在全角空格
##d={}        #本行代码题目已经给出的
##for word in lines:
##    if word in fuhao:
##        continue
##    else:
##        d[word] = d.get(word,0) + 1
##ls = list(d.items())
##ls.sort(key = lambda x:x[1],reverse = True)
##tongji = open('命运-频率统计.txt','w')
##for a in ls:    #将排序后的内容依次按照格式要求写入文件中
##    a_new = a[0] +':'+str(a[1])+','
##    tongji.write(a_new)
##tongji.close()
