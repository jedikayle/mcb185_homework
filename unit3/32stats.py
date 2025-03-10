# 32stats.py by Jedikayle
import math
import sys

numbers = [] # sets a list, always square brackets[]
for arg in sys.argv[1:]:
    f = float(arg) # convert argument to a flot
    numbers.append(f) # add it to the numbers list
print('# of values',len(numbers))

min = numbers[0] # must be this way because min = 0 includes 0 in the argument
max = numbers[0]
for val in numbers[1:]:
    if val < min: min = val
    if val > max: max = val
print('min:',min)
print('max:',max)

total = numbers[0] # gives the wrong mean when initialized by total = 0
for val in numbers[1:]: 
    total += val
mean = total/len(numbers)
print('mean:',mean)

variance = 0
for val in numbers[1:]: 
    variance += (val - mean) ** 2 # this is the numerator of the variance formula
stddev = math.sqrt(variance/(len(numbers)-1))
print('sd:',stddev)

numbers.sort() # sort numbers in ascending order
n = len(numbers) # find length of numbers list
if n % 2 == 1: # odd
    median = numbers[n//2]
else: # even
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2  # The average of the two middle elements
print('median:',median)

numbers.sort(reverse=True)  # sort numbers in descending order
total = sum(numbers)
cumulativelength = 0
half = total / 2  # use the total count of elements, not their sum
n50 = 0

for num in numbers:
    cumulativelength += num  # count the number of elements instead of summing their values
    if cumulativelength >= half:
        n50 = num
        break
print('N50:',n50)