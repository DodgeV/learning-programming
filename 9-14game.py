import random
rand2 = random.randint(1,100)
guess = int(input ('guess a number:'))
count = 1
while guess != rand2:
    if guess > rand2:
        print('be smaller')
    else:
        print('be bigger')
    guess = int(input('guess a number'))
    count += 1
print('bingo with %d times'%(count))
