# 24savingthrows.py by Jedikayle

'''
Write a program that simulates saving throws against DCs of 5, 10, and 15.
Make a table showing the probability of success normally, with advantage,
and with disadvantage.
'''
import random

trials = 100
def savingthrowsnormal(dc):
    success = 0
    for i in range(trials):
        roll1 = random.randint(1,20)
        if roll1 >= dc:
            success += 1
    print(i,dc,roll1,'success', success/trials)
    print('probability of success is', success/trials)



trials = 100
def savingthrowsadvantage(dc):
    success = 0
    for i in range(trials):
        roll1 = random.randint(1,20)
        roll2 = random.randint(1,20)
        if roll1 < roll2:
            roll1 = roll2
        if roll1 >= dc:
            success += 1
    print(i,dc,roll1,roll2,'success', success/trials)
    print('probability of success with advantage is', success/trials)


trials = 100
def savingthrowsdisadvantage(dc):
    success = 0
    for i in range(trials):
        roll1 = random.randint(1,20)
        roll2 = random.randint(1,20)
        if roll1 > roll2:
            roll1 = roll2
        if roll1 >= dc:
            success += 1
    print(i,dc,roll1,roll2,'success', success/trials)
    print('probability of success with disadvantage is', success/trials)

# the ones below do the same things as above
rolls = savingthrowsnormal, savingthrowsadvantage, savingthrowsdisadvantage
for dc in range(5,16,5):
    for roll in rolls:
        roll(dc)


for dc in range(5,16,5):
    adv = 0
    dis = 0
    norm = 0
    for i in range(trials):
        r1=random.randint(1,20)
        r2=random.randint(1,20)
        if r1 >= dc: norm += 1
        if r1 >= dc and r2 >= dc: dis += 1
        if r1 >= dc or r2 >= dc: adv +=1
    print(norm/trials,adv/trials,dis/trials) 