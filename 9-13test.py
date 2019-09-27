f = open('NOTE4.txt')
speak = []
say = []
count = 1

def new():
    speak_file = 'speak_' + str(count) + '.txt'
    say_file = 'say_' + str(count) + '.txt'

    speak_thing = open(speak_file, 'w')
    say_thing = open(say_file, 'w')

    speak_thing.writelines(speak)
    say_thing.writelines(say)

    speak_thing.close()
    say_thing.close()

for i in f:
    if i[:4] != '====':
        [a,b]=i.split(":",1)
        if a == 'speak':
            speak.append(b)
        else:
            say.append(b)
    else:
        new()
        speak = []
        say = []
        count += 1

new()
f.close()
