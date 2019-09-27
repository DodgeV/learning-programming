import os
member2 = dict()
def find(start,target):
    os.chdir(start)
    member1 = os.listdir(os.path.curdir)
    for a in member1:
        member2.setdefault(os.path.splitext(a)[0],os.path.splitext(a)[1])
        if member2[os.path.splitext(a)[0]] == target:
            print(start+os.sep+a)
        elif os.path.isdir(a):
            find(a,target)
            os.chdir(os.pardir)
start = input('请输入路径:')
target = input('请输入目标文件扩展名:')
find(start,target)
