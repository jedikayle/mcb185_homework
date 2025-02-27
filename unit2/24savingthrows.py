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
savingthrowsnormal(5)
savingthrowsnormal(10)
savingthrowsnormal(15)


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
savingthrowsnormal(5)
savingthrowsnormal(10)
savingthrowsnormal(15)

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
savingthrowsnormal(5)
savingthrowsnormal(10)
savingthrowsnormal(15)