# monty pi-thon
import random 

inside = 0 # set initial value for inside and outside
total = 0

while True: # infinite loop
    total += 1
    x = random.random() # random between 0 and 1
    y = random.random() # random y between 0 and 1

    distance = x**2 + y**2 # squared distance from (0,0) d^2 = x^2 + y^2

    if distance <=1: # if distance <1 then point inside circle
        inside += 1 # this means inside = inside + 1
        piestimate = 4 * (inside / total)
    print(piestimate)