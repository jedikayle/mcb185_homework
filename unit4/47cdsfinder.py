# 47cdsfinder.py by Jedikayle

'''
Write a program that finds open reading frames in the E. coli genome.

Input: multi-FASTA file of DNA
Output: multi-FASTA file of proteins
Must perform a six-frame translation
Proteins must be at least 100 amino acids long
Proteins must start with 'M' and end with '*'
Deflines must have unique identifiers
The command line should look something like this.
'''

import sys
import sequence
import mcb185

s = sys.argv[1]  # Get input FASTA file

def cdsfinder(seq, defline, count):
    seqs = seq.split('ATG')  
    seqs.pop(0)  # Remove sequence before the first ATG
    orfs = []
    
    for orf in seqs:
        aa = sequence.translate(orf)  # Translate ORF
        if aa:  #Avoid None outputs
            if aa[-1] == '*':  #Stop codon 
                orfs.append(f"> {defline}-prot-{count}\nM{aa}") # format output
            else:  #No stop codon
                orfs.append(f"> {defline}-prot-{count}\nM{aa}")

    return "\n".join(orfs)

#original strand
count = 0
for defline, seq in mcb185.read_fasta(s):
    print(cdsfinder(seq, defline, count))
    count += 1

#reverse complement
count = 0
for defline, seq in mcb185.read_fasta(s):
    revcomp_seq = sequence.revcomp(seq)
    print(cdsfinder(revcomp_seq, defline, count))
    count += 1