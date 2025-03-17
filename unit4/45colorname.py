# 45colorname.py by Jedikayle
import sys

colorfile = sys.argv[1] # colorfile path
R = int(sys.argv[2]) # red input value
G = int(sys.argv[3]) # green input value
B = int(sys.argv[4]) # blue input value

# distance function
def dtc(P,Q):
    d = 0
    for p, q in zip(P,Q): # P = (R, G, B), Q = (r, g, b)
        d += abs(p - q) # sum absolute differences btwn RGB vals
    return d

# initializing variables
mindistance = 246 # initializing the closest distance to max val
closestcolor = None # saying that there isnt currently a closest color

# opening color file and looking
with open(sys.argv[1], 'rt') as fp: # opening compressed color file in compressed mode
    for line in fp: # need to read each line so we must work in the loop
        colorline = line.split('\t') # splits line in order of name, colorcode, r val, g val, and b val; \t refers to 'tab'
        name, colorcode, rgb = colorline # defining each part of the colorline
        r,g,b = rgb.split(',') # splitting rgb in r,g,b
        r, g, b = int(r), int(g), int(b) # converting r,g,b to integers
    
        distance = dtc((R,G,B), (r,g,b)) # using dtc() to find distance btwn RGB & rgb

        if distance < mindistance: 
            mindistance = distance # then the mindistance becomes the new distance
            closestcolor = name # then the name of that line gets stored as the closest color

print(closestcolor, mindistance)
    
'''
note:
colors are formatted like this
aqua	#00FFFF	0,255,255
aquamarine	#7FFFD4	127,255,212
azure	#F0FFFF	240,255,255

.tsv stands for tab separated files
\t = 'tab'

rgb values range from 0 to 255

'''