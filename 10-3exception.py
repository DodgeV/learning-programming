try:
    sum = 1 + '1'
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错了！\n错误的原因是：'+str(reason))
except TypeError as reason:
    print('又出错了\n理由是'+str(reason))
except (OSError,TypeError):
    print('出错了')
finally:
    print('这一行不管出不出错，必定执行')