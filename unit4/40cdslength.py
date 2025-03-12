# 40cdslength.py

import gzip
import sys

with gzip.open(sys.argv[1],'rt') as fp: # open compressed file in text mode ('rt' = read text)
    for line in fp: # loops through each line in the file
        if line[0] == '#': continue # checks if first character of the line is #, skips and move to next line
        words = line.split() # splits line into a list of words sep by spaces
        if words[2] != 'CDS': continue # third column of gff file tells us what type of feature it is, if not coding sequence then it skips
        beg = int(words[3]) # starts @ column 4 of gff, converts fr strings to in
        end = int(words[4]) # starts @ column 5 of gff
        print (end - beg + 1) # length = end - beginning + 1

'''
 The with command automatically closes the file when done
 the continue command immediately skips irrelevant lines
'''