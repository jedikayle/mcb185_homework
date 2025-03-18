# 46dust.py by Jedikayle

'''
Prior to doing sequence searches, people often mask low complexity sequence to prevent finding huge numbers of meaningless alignments. One of the common programs that does this task is called dust. Write a python version.

Input: multi-FASTA file of DNA
Output: multi-FASTA file of DNA with low complexity regions masked
Change all low-complexity regions to 'N' in the output
Provide parameters for fasta file, window size, and entropy
'''
import sys
import math
import mcb185

w = int(sys.argv[2])
entropy = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for nt in seq:
        for nt in range(len(seq) - w + 1):
            s = seq[nt:nt+w]
            a = s.count('A')
            c = s.count('C')
            g = s.count('G')
            t = s.count('T')
            nts = a, c, g, t
            for i in nts:
                hlist = []
                if i == 0: continue
                p = i/w
                h = p * math.log2(p)
                hlist.append(h)
            H = -1 * math.fsum(hlist)
            if H < entropy:
                newseq = seq.replace(seq[nt], 'N')
            print(newseq)


