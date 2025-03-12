# 42ntcomp.py
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    gc = 0
    for nt in seq:
        if nt == 'C' or nt == 'G': gc +=1
    print(name, gc/len(seq))