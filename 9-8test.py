f = open('NOTE4.txt')

speak = []
girl = []
count = 1

for each in f:
    if each[:3] != '===':#str's split
        [role,line] = each.split(":",1)#split one time
        if role == 'speak':
            speak.append(line)
        else :
            girl.append(line)
    else:#ctrl+s separately
        file_name_boy = 'speak_'+str(count)+'.txt'
        file_name_girl = 'girl_'+str(count)+'.txt'

        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')

        boy_file.writelines(speak)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()
        
        speak = []
        girl = []
        count += 1
        
file_name_boy = 'speak_'+str(count)+'.txt'
file_name_girl = 'girl_'+str(count)+'.txt'

boy_file = open(file_name_boy,'w')
girl_file = open(file_name_girl,'w')

boy_file.writelines(speak)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()
        
f.close()
