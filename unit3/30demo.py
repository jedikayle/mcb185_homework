# strings
s = 'hello world'
print(s)

s1 = 'hey "dude"' # put double quotes inside single quotes
s2 = 'dont tell me what to do'
print(s1,s2)

print('hey "dude" don\'t tell me what to do')
# backslashes indicate special characters

# string methods
print(s.upper()) # uppercase version of string s, defined on line 2

print(s.replace('o','')) # removes letter o and replaces with a blank, "hell wrld"
print(s.replace('o','').replace('r', 'i')) # after first replacement we are doing a second replacement "hell wlid"

# string formatting
import math

print(f'{math.pi}') # prints as is
print(f'{math.pi:.3f}') # 3 decimal places
print(f'{1e6*math.pi:e}') # scientific notation
print(f'{"hello world":>20}') # right justify w space filler
print(f'{"hello workd":.>20}') # right justify w dot filler
print(f'{20:<10} {10}') # left justify

print('{} {:.3f}'.format('str.format', math.pi)) #str.format
# {} is replaced by 'str.format' and {:.3f} ensures 3 dec places for pi

print('%s %.3f' % ('printf', math.pi)) # legacy format %s = stirng %.3f = 3 decimal places

#indexes = position of a character in a string
#indexing starts at 0, not 1
seq = 'GAATTC'

print(seq[0], seq[1]) # seq[0]=G seq[1]=A
print(seq[-1]) # negative index, counts backwards seq[-1]=C

for nt in seq: # loops through each character in seq
    print(nt, end='') # prints each new character without new line
print() # moves to next line after the loop

for i in range(len(seq)): 
    print(i, seq[i])
''' len(seq) returns length of seq
range(len(seq)) generates numbers from 0 to 5 (indexes)
seq[i] gets character at index i'''

# slice = way to extract a subset
s = 'ABCDEFGHIJ' 
print(s[0:5]) # starts a index 0 and ends before index 5
#output ABCDE

print(s[0:8:2]) # start a 0, end before 8, skip by 2
#output ACEG

print(s[0:5], s[:5]) # both ABCDE, second is shortcut notation
print(s[5:len(s)], s[5:]) # both FGHIJ

print(s, s[::], s[::1], s[::-1]) 
''' first 3 are equivalents, 
last returns reverse output'''

# slice a DNA string into codon
dna = 'ATGCTGTAA' 
for i in range(0, len(dna), 3): # loop through indexes from 0 to len(dna to step of 3)
    codon = dna[i:i+3] # define codon and slicing string fr index to i to i+3
    print(i, codon) # print starting index (i) and extracted codon
'''
i = 0 -> dna[0:3] = 'ATG'
i = 3 -> dna[3:6] = 'CTG'
i = 6 -> dna[6:9] = 'TAA'
'''

# tuples = immutable container like strings
tax = ('Homo','sapiens',9606) 
print(tax) # note there is parentheses in the output

print(tax[0]) # can be indexed like strings
print(tax[::-1]) # can be sliced like strings

# enumerate() = indexing a sequence
nts = 'ACGT'
for i in range(len(nts)): # length of nts is 4
    print(i, nts[i]) # gives values from 0 to before 4

#below does same as above but cleaner
for i, nt in enumerate(nts):
    print(i, nt)

# zip() = pairing two sequences
names = ('adenine','cytosine','guanine','thymine')
for i in range(len(names)):
    print(nts[i], names[i])

# below does same as above but cleaner
for nt, name in zip(nts, names): # pairs elements from both nts & names tuples
    print(nt, name)

for i, (nt, name) in enumerate(zip(nts,names)): #adding an index to paired elements
    print(i, nt, name) # output index, nt, name (ex. 0 A adenine)

# lists = uses [square brackets] and mutable, sim to tuples
nts = ['A','T','C']
print(nts)
nts[2] = 'G' # changes C -> G
print(nts)

nts.append('C') #listname.append() = adds element to end of list
print(nts)

last = nts.pop() # listname.pop() removes and returns the last element
print(last)
print(nts)

nts.sort() #listname.sort() = sorts in ascendings order
print(nts)

nts.sort(reverse=True) # sorts in descending order

nucleotides = nts # setting that both nucleotides and nts refer to the same list
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list() # list() w/o arguments generate empty list
print(items)
items.append('eggs') # adds eggs to the list
print(items)

stuff = [] # can also create empty lists with square brackets
stuff.append(3) # adds 3 to the list
print(stuff)

alph = 'ABCDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph) # converts string into a list of characters
print(aas)

# split() and join()
text = 'good day to you'
words = text.split() #stringname.split() = converts string into a list of words
print(words)

line = '1.41,2.72,3.14'
print(line.split(',')) # splits on the comma

s = '-'.join(aas) # joined by - delimiter
print(s) # Output: 'A-C-D-E-F-G-H-I-K-L-M-P-Q-R-S-V-W'
s = ''.join(aas) # joined by blank delimeter
print(s) # Output: 'ACDEFGHIKLMPQRSVW'

# searching
if 'A' in alph: print('yay')
if 'a' in alph: print('no') # no output bc 'a' is not in alph

# index() = for lists and strings
print('index G?', alph.index('G')) # stringname.index() = returns index of where element occurs
# print('index Z?', alph.index('Z')) -> returns error bc Z is not in string

# find() = only for strings
alph = 'ABCDEFGHIKLMPQRSVW'
print('find G?', alph.find("G")) 
print('find Z?', alph.find("Z")) # returns -1 to indicate it does not exist