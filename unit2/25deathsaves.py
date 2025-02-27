# 25deathsaves.py by Jedikayle
import random

stable = 0
rounds = 100 # interchangeable
revivals = 0
death = 0

for i in range(rounds): # outside for loop
    successes = 0 # initialization
    failures = 0
    for turn in range(6): # run 6 turns
        roll = random.randint(1,20)

        if roll == 1: # rolling a 1 = 2 fails
            failures += 2 # means failures = failures + 2
        elif roll == 20: # rolling a 20 means revived
            revivals += 1
            break
        elif roll >= 10: # rolling > 10 = 1 success
            successes += 1
        else: # if roll < 10
            failures += 1 # means failures = failures + 1

        if successes == 3: # if you get three successes you are stable
            stable += 1
            break
        elif failures >= 3:
            death += 1
            break

print('Probability of death', death/rounds)
print('Probability of being stabilized', stable/rounds)
print('Probability of being revived', revivals/rounds)