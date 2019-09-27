m = []
n = []
for i in range(1,100):
    for a in range(1,i):
        if i%a == 0:
            m.append(a)
    if sum(m) == i:
        n.append(i)
    m = []
print('1到100之间的完数如下:',n)
