 # practice problems
import math
def triangularnumber(n):
    tri = 0
    for i in range(n+1): # loop from 0 to n, all # up to n is summed
        tri = tri + i # add current number i to tri
    return tri
print(triangularnumber(4)) # output 10

def factorial(n):
    if n == 0: return 1 # special condition 0! = 1
    fac = 1
    for i in range(1, n + 1): # range stops right before n + 1
        fac = fac * i
    return fac
print(factorial(4)) # output 4 x 3 x 2 x 1 = 21

def poissonprob(n,k):
    return n**k * math.e**-n / (factorial(k))
print(poissonprob(3,2)) # output 0.22

def nchoosek(n, k):
    return (factorial(n)) / (factorial(k) * factorial(n-k))
print(nchoosek(5,2)) # output 10

def eulers(limit):
    e = 0 # starting number
    for n in range(limit):
        e = e + 1/ factorial(n) # each iteration we add 1/ factorial(n) to e
    return e
print(eulers(5)) # output e = 2.708

def isprime(n):
    n = 0
    for denominator in range(2, n//2 + 1): # iterates through possible divisors
        if n % denominator == 0: # if n is divdsible by denominator range, it is not a prime number
            return False
    return True
print(isprime(7)) # output true

def nilakantha(limit):
    pi = 3 # starting
    for i in range(1, limit + 1): # iteration begins at one and goes up to limit
        n = 2 * i # numerator
        d = n * (n+1) * (n+2) # denominator
        if i % 2 == 0: # checks if i is even or odd bc nilakantha alternates btwn add and subtract
            pi = pi - 4 / d # subtract if i is even
        else:
            pi = pi + 4 / d # add if i is odd
    return pi
print(nilakantha(3)) # 3.145238095238095

# random numbers
import random

for i in range(5): # "roll" 5 times
    print(random.random()) # produces rand numb between 0 & 1

for i in range(3): # "roll" 3 times
    print(random.randint(1,6)) # (random.rantint(a,b))
    # generates rand numb between 1 and 6

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

# more practice