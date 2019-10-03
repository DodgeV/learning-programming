import os
print(os.getcwd())

import pickle
f = open('record.txt','r',encoding='UTF-8')#此处加一句encoding防止报错UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 4: illega
count = 1
boy = []
girl = []
def save_file(a,b,count):
    f_b = open('boy_'+ str(count) + '.txt','wb')
    f_g = open('girl_'+ str(count) + '.txt','wb')
    pickle.dump(a,f_b)
    pickle.dump(b,f_g)
    f_b.close()
    f_g.close()
for i in f:
    if i[:3] != '===':
        m = i.split(":")
        if m[0] == '小甲鱼':
            boy.append(m[1])
        else:
            girl.append(m[1])
    elif i[:3] == '===':
        save_file(boy,girl,count)
        count += 1
        boy = []
        girl = []
save_file(boy,girl,count)
f.close()
