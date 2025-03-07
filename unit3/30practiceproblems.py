# unit 3 practice problems by Jedikayle

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)

print('minimum value of the list')
def minimum(vals):
    mini = vals[0]
    for val in vals[1:]:
        if val < mini: mini = val
    return mini
print(minimum(numbers))

print('min and max values of the list')
def minmax(vals):
    mini = vals[0] # set point to start looking for min and max
    max = vals[0]
    for val in vals[1:]:
        if val < mini: mini = val
        if val > max: max = val
    return mini, max
print(minmax(numbers))

print('mean values of a list')
def mean(vals):
    return sum(vals)/len(vals)
print(mean(numbers))

# below is the command that prof expects, but above is faster
def altmean(vals):
    total = 0 # set starting point
    for val in vals: total += val # loop that goes through each value and adds it to total
    return total/len(vals)
print(altmean(numbers))

print('entropy of a probability distribution')
import math

probdist = [0.2, 0.3, 0.5]
print(probdist)

def entropy(probs):
    h = 0 # intialize entropy
    for p in probs: # The for loop iterates over each probability and adds the calculated entropy term (p * log2(p)) to h
        h -= p * math.log2(p)
        return h
print(entropy(probdist)) # higher entropy means more uncertainty

print('kullback-leibler distance') 
# when you have two probability dist and want to understand how different they are

def dkl(p,q):
    d = 0
    for p,q in zip(p,q): # zip compares two lists
        d += p * math.log2(p/q)
        return d
    
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = [0.1, 0.3, 0.4, 0.2]
print(p1,p2)

print(dkl(p1,p2))

