# 33birthday.py by Jedikayle 
import random
import sys

trials = int(sys.argv[1]) # setting 1st CLA to # of trials
days = int(sys.argv[2]) # setting 2nd CLA to # days
people = int(sys.argv[3]) # setting 3rd CLA to # people

print("trials:",trials,"days:",days,"people:",people)

for trial in range(trials):

    birthdays = []

    #generate a random bday for everyone in the trial
    for day in range(people): # loop over the number of people
        birthdays.append(random.randint(1,365)) # append adds values to the bday list

    match = False # initialize boolean to false bc true or false
    successes = 0
    for i in range(0, len(birthdays)):
        for j in range(i + 1, len(birthdays)): # start a i + 1 to avoid self comparison
            if birthdays[i] == birthdays[j]: 
                match = True # indicate we found a match
                break # break the loop and go again if a match is found

        if match:
            break

    if match:
        successes += 1 # if we find a match within a trial then we add one success

probability = successes/trials
print('probability of 2 people w same bday:', probability)

