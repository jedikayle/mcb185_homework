# 34birthday.py by Jedikayle
import random
import sys

trials = int(sys.argv[1]) # setting 1st CLA to # of trials
days = int(sys.argv[2]) # setting 2nd CLA to # days
people = int(sys.argv[3]) # setting 3rd CLA to # people

print("trials:",trials,"days:",days,"people:",people)

successes = 0 # initialize keep track how many times 2+ ppl share bday

for trial in range(trials): # initialize a loop through all of the trials

    # make calendar
    calendar = [0] * days # calendar list, note: 0 counts as a value remember to skip going forward

    # assign random bdays
    for day in range(people): # loops over number of people
        birthday = random.randint(1,365) 
        calendar[birthday - 1] +=1 # -1 bc we need to avoid 0th day, increment value at day

    # check for shared bday
    match = False # boolean, start by assume no one share a bday
    for i in range(len(calendar)): # loop goes over each day in calendar list
        if calendar[i] > 1: 
            match = True # if there is > 1 person on same day, then it is a match
    if match: 
        successes +=1

probability = successes/trials
print('probability of 2 people w same bday:', probability)