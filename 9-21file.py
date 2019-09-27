f = open('D:\\Users\\向致承\\Documents\\python\\NOTE4.txt')
speak = []
say = []
count = 1
for i in f:
    if i[:3] != '===':
        a = i.split(':')[0]
        b = i.split(':')[1]
        if i[:5] == 'speak':
            speak.append(b)
        elif i[:3] == 'say':
            say.append(b)
    else:
        speakfile = 'speak' + str(count) +'.txt'
        sayfile = 'say' + str(count) +'.txt'
        sp_file = open(speakfile,'w')
        sa_file = open(sayfile , 'w')
        sp_file.writelines(speak)
        sa_file.writelines(say)
        sp_file.close()
        sa_file.close()
        speak = []
        say = []
        count += 1
speakfile = 'speak' + str(count) +'.txt'
sayfile = 'say' + str(count) +'.txt'
sp_file = open(speakfile,'w')
sa_file = open(sayfile , 'w')
sp_file.writelines(speak)
sa_file.writelines(say)
sp_file.close()
sa_file.close()
f.close()

