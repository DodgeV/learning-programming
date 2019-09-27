import os
member4 = dict()
member1 = os.listdir(os.curdir)
for i in member1:
    if os.path.isdir(i):
        member4.setdefault('文件夹',0)
        member4['文件夹'] += 1
    else:
        exp = os.path.splitext(i)[1]
        member4.setdefault(exp,0)
        member4[exp] += 1
for i in member4.keys():
    print('该文件夹共有[%s]文件%d个'%(i,member4[i]))
