import os
def find(start,target):
    os.chdir(start)
    member1 = os.listdir(os.path.curdir)
    for i in member1:
        if i == target:
            print(os.getcwd()+ os.sep + i)
        elif os.path.isdir(i):
            find(i,target)
            os.chdir(os.pardir)
start = input('请输入文件夹:')
target = input('请输入文件名:')
find(start,target)
