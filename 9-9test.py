def save(speak,girl,count):
    file_name_boy = 'speak_'+str(count)+'.txt'
    file_name_girl = 'girl_'+str(count)+'.txt'

    boy_file = open(file_name_boy,'w')
    girl_file = open(file_name_girl,'w')

    boy_file.writelines(speak)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def split(file_name):
    
    f = open(file_name)

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
            save(speak,girl,count)
            
            speak = []
            girl = []
            count += 1
    save(speak,girl,count)
    f.close
        
split('note4.txt')
