# 21fizzbuzz.py activity by Jedikayle
import math

for i in range(101):
    if i % 3 == 0 and i % 5 == 0: print(i,'FizzBuzz')
    elif i % 3 == 0: print(i, 'Fizz')
    elif i % 5 == 0: print(i, 'Buzz')
    else: print(i)
