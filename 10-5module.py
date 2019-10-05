def multinverse(num):
    return 1/num
#我们通常在模块里面写一些执行代码是为了测试模块的功能。这被称为单元测试。
# 在常规项目开发中，单元测试是代码质量保证的前提
print(__name__)
if (__name__ == '__main__'):
    import sys
    print (sys.argv)
    if len(sys.argv) > 1:
        print(multiinverse(sys.argv[1]))
