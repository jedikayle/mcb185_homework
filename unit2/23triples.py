# 23triples.py by Jedikayle
'''
Write a program that finds all Pythagorean triples for triangles
with sides a and b less than 100. For example, 3, 4, 5 is a triple: 
3^2 + 4^2 = 5^2. Hint: all sides, including the hypotenuse, 
must be integers. A good way to test for an integer is like: if c % 1 == 0
'''
import math

for a in range(1,100):
    for b in range(a,100):
        c = math.sqrt(a**2 + b**2) # compute c using pythagorean theorem
        if c % 1 == 0: # test if c is an integer
            print(a, b, int(c)) # int(c) removes ".0" at end of number