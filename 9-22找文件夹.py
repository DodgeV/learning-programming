import os
def findfile(start,dir1):
    os.chdir(start)
    for i in os.listdir(os.path.curdir):
        if i == dir1 and os.path.isdir(dir1):
            print(os.getcwd() + os.sep + i)
        elif os.path.isdir(i):
            findfile(i,dir1)
            os.chdir(os.pardir)
start = input('请输入文件夹:')
dir1 = input('请输入文件夹名:')
findfile(start,dir1)
#print('该文件夹[%s]文件大小为[%d]BYTE'%(i,member1[i]))