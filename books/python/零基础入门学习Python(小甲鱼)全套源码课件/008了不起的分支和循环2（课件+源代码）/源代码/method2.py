score = int(input('请输入您的分数：'))
if 100 >= score >= 90:
    print('A')
else:
    if 90 > score >= 80:
        print('B')
    else:
        if 80 > score >= 60:
            print('C')
        else:
            if 60 > score >= 0:
                print('D')
            else:
                print('输入错误！')