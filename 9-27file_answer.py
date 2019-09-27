def file_write(file_name):
    f = open(file_name, 'w')
    print('请输入内容【单独输入\':w\'保存退出】：')

    while True:
        write_some = input()
        if write_some != ':w':
            f.write('%s\n' % write_some)
        else:
            break

    f.close()

file_name = input('请输入文件名：')
file_write(file_name)
