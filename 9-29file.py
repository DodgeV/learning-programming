file = input('请输入文件名:')
number = str(input('请输入需要显示该文件的第几行:'))
f = open(file)
a = str(number.split(':')[0]
b = number.split(':')[1]
if a == '':
    a = 0
elif b == '':
    b = 0
for i in list(f)[a:b]:
    print(i)