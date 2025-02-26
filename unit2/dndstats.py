# D&D Stats by Jedikayle

import random

# 3D6: roll 3 six-sided dice
def roll3d6():
    total = 0 # set initial value
    for i in range(3): # roll 0th 1st 2nd
        n = random.randint(1,6) # set boundary
        total += n # this means total = total + n
    return total
print(roll3d6())

# 3D6r1: roll 3 six-sided dice, but re-roll any 1s
def roll3d6r1():
    total = 0
    for i in range(3):
        n = random.randint(1,6)
        if n == 1:
            n = random.randint(1,6)
        total += n
    return total
print(roll3d6r1())

# 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
def roll3d6x2():
    total = 0
    for i in range(3):
        a = random.randint(1,6)
        b = random.randint(1,6)
        if a < b: a = b
        total += a
    return total
print(roll3d6())

# 4D6d1: roll 4 six-sided dice, dropping the lowest die roll
def lowestdie(a,b,c,d):
    if a <= b and a <= c and a <= d: return a
    if b <= c and b <=d: return b
    if c <=d: return c
    else: return d
def roll4d6d1():
    total = 0
    for i in range(3):
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        d = random.randint(1,6)
        total = a + b + c + d
        finaltotal = total - (lowestdie(a,b,c,d))
    return finaltotal
print (roll4d6d1())
