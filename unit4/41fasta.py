# 41fasta.py

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]): # loop that iterates over the seqeunces in the fasta file
    print(defline[:30], seq[:40], len(seq)) # defline[:30] prints out first 30 characters of defline string, seq[:40] prints first 40 characters of seqeunce

'''
Each iteration of the for loop retrieves the next record from the
FASTA file. Each record is returned as a tuple containing the
definition line and the sequence (as a single string, not a bunch of
lines). The function works with both normal and compressed files.
'''