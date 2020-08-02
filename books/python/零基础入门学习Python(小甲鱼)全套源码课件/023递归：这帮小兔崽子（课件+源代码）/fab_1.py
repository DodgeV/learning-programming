def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print('输入有误！')
        return -1

    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    
    return n3

result = fab(45)
if result != -1:
    print('总共有%d对小兔崽子诞生！' % result)
