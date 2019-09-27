file_name = input('请输入文件名:')
file_content2 = input('请输入内容【单独输入":w"保存退出】:')

def creat_file(name,file_content):
    f = open(name,'w')
    while file_content != ':w':
        f.writelines('%s\n'%(file_content))
        file_content = input('请输入内容【单独输入":w"保存退出】:')
    f.close()

creat_file(file_name,file_content2)