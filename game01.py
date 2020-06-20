import random
secret = random.randint(1,10)
print ('Game Begin'.center(25))
temp = input ('please guess a number from 1 to 10:')
p = int(temp)
if p == secret:
    print ('Bingo')
elif 1<= p <= secret:
    print ('be bigger')
elif secret <= p <= 10:
    print ('be smaller')
def compare(temp):
    temp = input ('try it again:')
    p = int(temp)
    if p == secret:
        print ('Bingo')
    elif 1<= p <= secret:
        print ('be bigger')
    elif secret <= p <= 10:
        print ('be smaller')
    else:
        print ('please guess from 1 to 10')    
while 1 <= p <= 10 and p != secret:
    compare(temp)
while p < 1 or p > 10:
    temp = input ('try it again from 1 to 10:')
    p = int(temp)
    if p == secret:
        print ('Bingo')
    elif 1<= p <= secret:
        print ('be bigger')
    elif secret <= p <= 10:
        print ('be smaller')
while 1 <= p <= 10 and p != secret:
    compare(temp)
print ('Game Over'.center(25))