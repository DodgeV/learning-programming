import os
member2 = []
member3 = []
member4 = []
member1 = os.listdir('d:\\users\\向致承\\documents\\python')
#directionary = input('请输入待查找的初始目录:')
#file = input ('请输入需要查找的目标文件:')
for i in member1:
    a = i.split('.')
    member2.append(a)
for i in member2:
    n = len(i)
    if n >= 2:
        member3.append(i[-1])
    member4.append(i[0])
print('该文件夹共有py文件%d个'%member3.count('py'))
print('该文件夹共有txt文件%d个'%member3.count('txt'))
print('该文件夹共有zip文件%d个'%member3.count('zip'))


