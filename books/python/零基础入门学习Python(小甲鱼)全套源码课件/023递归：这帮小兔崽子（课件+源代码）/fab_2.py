def fab(n):
    if n < 1:
        print('输入有误！')
        return -1

    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

result = fab(35)
if result != -1:
    print('总共有%d对小兔崽子诞生！' % result)
