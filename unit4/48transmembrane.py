# 48transmembrane.py by Jedikayle

'''
Write a program that predicts which proteins in a proteome are transmembrane.
 Transmembrane proteins are characterized by having:

a hydrophobic signal peptide near the N-terminus
other hydrophobic regions to cross the plasma membrane

signal peptide: 8 aa long, average KD >= 2.5, first 30 aa
transmembrane region: 11 aa long, average KD >= 2.0, after 30 aa
Both the signal peptide and the transmembrane regions are alpha-helices 
Therefore, they do not contain proline.

Isoleucine		I	4.5
Valine			V	4.2
Leucine			L	3.8
Phenylalanine	F	2.8
Cysteine		C	2.5
Methionine		M	1.9
Alanine			A	1.8
Glycine			G	-0.4
Threonine		T	-0.7
Serine			S	-0.8
Tryptophan		W	-0.9
Tyrosine		Y	-1.3
Proline			P	-1.6 *** Both the signal peptide and the transmembrane regions are alpha-helices Therefore, they do not contain proline.
Histidine		H	-3.2
Glutamic acid	E	-3.5
Glutamine		Q	-3.5
Aspartic acid	D	-3.5
Asparagine		N	-3.5
Lysine			K	-3.9
Arginine		R	-4.5
'''

import sys
import mcb185
import sequence

def hydrophobicity(seq):
    aas = 'IVLFCMAGTSWYPHEQDNKR'
    kds = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]
    return [kds[aas.index(aa)] for aa in seq]

def avg_kd(seq):
    return sum(hydrophobicity(seq)) / len(seq)

def is_transmem(seq):
    sigpep_region = seq[:30]
    transmem_region = seq[30:]

    for i in range(len(sigpep_region) - 8 + 1): #Check signal peptide (8 aa, KD >= 2.5, no P)
        sigpep = sigpep_region[i:i+8]
        if 'P' not in sigpep and avg_kd(sigpep) >= 2.5:
            break
    else:
        return False 

  
    for i in range(len(transmem_region) - 11 + 1): #check transmembrane region (11 aa, KD >= 2.0, no P)
        transmem = transmem_region[i:i+11]
        if 'P' not in transmem and avg_kd(transmem) >= 2.0:
            return True 

    return False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if is_transmem(seq):
        print(defline)
        print(seq[:50])