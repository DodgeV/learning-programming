m = []
h = ''
def change(n):
    number = int(n) // 2
    member = int(n) % 2
    m.append(member)
    if number > 0:
        return change(number)
    elif number == 0:
        m.reverse()
        for i in m:
            global h
            h  += (str(i))
        return int(h)
n = input('please get a number:')
print('%s的2进制数为%d'%(n,change(n)))