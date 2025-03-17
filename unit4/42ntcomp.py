# 42ntcomp.py
import sys
import mcb185

'''
Let's write a program 42ntcomp.py that calculates the composition 
of nucleotides in a FASTA file.The first one calculates the GC
composition of each sequence separately.
'''

# counting w str.count(); other vairations are below
for defline, seq in mcb185.read_fasta(sys.argv[1]): # loops over each seq in fasta file
    defwords = defline.split() # takes the defline (which is a string) and splits it into words based on spaces, resulting list stored in a variable called defwords
    name = defwords[0] # extracts the first word as the name
    print(name, end=' ')
    for nt in 'ACGTN':
        print(seq.count(nt)/len(seq), end=' ')
    print()
    
''' 
replace after line 13, same method using lists as counts
    counts = [0,0,0,0,0] # A C T G N
    for nt in seq:
        if nt == 'A': counts[0] += 1
        elif nt == 'C': counts[1] += 1
        elif nt == 'G': counts[2] += 1
        elif nt == 'T': counts[3] += 1
        else: counts[4] += 1
    print(name, end=' ')
    for n in counts: print(n/len(seq), end=' ')
    print()

indexing w str.find()
 nts = 'ACGTN'
    counts = [0] * len(nts)
    for nt in seq:
        idx = nts.find(nt)
        counts[idx] += 1
    print(name, end=' ')
    for n in counts: print(n/len(seq), end =' ')
    print()

counting any letter using list.index()
nts = []
    counts = []
    for nt in seq:
        if nt not in nts:
            nts.append(nt)
            counts.append(0)
        idx = nts.index(nt)
        counts[idx] += 1
    print(name)
    for nt, n in zip(nts, counts):
        print(nt, n, n/len(seq))
    print()
'''