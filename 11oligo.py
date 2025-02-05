'''
11oligo.py By Jedikayle
Write a function that returns the oligo melting temperature given the number of 
As, Cs, Gs, and Ts in the oligo. Use these two methods.
'''
import math

def tm(a, t, g, c):
    length = a+t+g+c
    if length <= 13: return (a+t)*2 + (g+c)*4
    if length > 13: return 64.9 + 41*(g+c -16.4) / (a+t+g+c)
print(tm(5,7,3,4)) # output = 44.61

