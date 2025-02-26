'''
12phred.py by Jedikayle
Write functions that convert quality value symbols into error rates and vice-versa. 
The ord() function returns the ASCII value of a letter. The chr() function turns an ASCII value into a letter.
Demonstrate the functions work by calling them several times. Edge cases should return None.
'''
import math

print('phred score to error probability')
def char_to_prob(c):
    return 2 ** (64-ord(c))
print (char_to_prob('A'))

print('error probability to phred score')
def prob_to_char(prob):
    return chr(int(-math.log2(prob)))
print (prob_to_char(0.5))

'''
A = 2^-1 65
B = 2^-2 66
C = 2^-3 67
'''