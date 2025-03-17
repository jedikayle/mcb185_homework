# 44skew.py by Jedikayle
import sequence
import mcb185
import sys

# efficient strategy
w = int(sys.argv[2])
g = 0
c = 0 # initializing counters


for defline, seq in mcb185.read_fasta(sys.argv[1]): # program.read_fasta(filename)
    g = seq[0:w].count('G') # seq[0:w] extracts first (w) nucleotides; similar to indexing but w a range
    c = seq[0:w].count('C') # .count('X') counts # of X's in seq
    print(sequence.gc_comp(seq[0:w]), sequence.gc_skew(seq[0:w]))
    for i in range(len(seq) - w - 1): # i is number of open windows, this loop iterates through each one
        if seq[i] == 'G':
            g -= 1 # g = g - 1
        if seq[i] == 'C':
            c -= 1
        if seq[i + w + 1] == 'G': # seq[i + w +1] refers to nt just after current window
            g +=1 # g = g + 1
        if seq[i + w +1] == 'C':
            c += 1
        gccomp = (g + c) / w # proportion of g's and c's in current window
        if g + c == 0: # avoid division by 0
            skew = 0
        else:
            skew = (g - c) / (g + c) # tells if g or c is more frequent
        print(i, gccomp, skew)

'''
notes: 
- seq is a string(immutable)

# inefficient strategy (sliding window approach)
w = int(sys.argv[2]) # represents window size in cla

for defline, seq in mcb185.read_fasta(sys.argv[1]): # read fasta file
    for i in range(len(seq) - w + 1):
        s = seq[i:i+w]
    print(i, sequence.gc_comp(s),sequence.gc_skew(s)) 
'''


