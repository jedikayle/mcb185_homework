# sequence.py by Jedikayle

# Transcription: Thymine -> Uracil
def transcribe(dna):
    return dna.replace('T', 'U')

# Reverse-Complement
def revcomp(dna):
    rc = [] # creates list to hold new sequence
    for nt in dna[::-1]: # steps backward througb sequence using slice syntax
        if nt == 'A': rc.append('T')
        elif nt == 'C': rc.append('G')
        elif nt == 'G': rc.append('C')
        elif nt == 'T': rc.append('A')
        else: rc.append('N')
    return ''.join(rc)

# Translation
def translate(dna):
    aas = [] # initialize empty list for amino acids
    for i in range(0, len(dna), 3): # steps through indices by 3
        codon = dna[i:i+3] # creates codon, 3 letter slice starting at index i
        if codon == 'ATG': aas.append('M') # start codon
        elif codon == 'TAA': aas.append('*') # stop codon
        elif codon == 'TAG': aas.append('*') # stop codon
        elif codon == 'TGA': aas.append('*') # stop codon
        else: aas.append('X') # unknown codon
    return ''.join(aas) # return aa sequence as a string

'''
alt way of doing translation code
def translate(dna):
    codons = ('ATG', 'TAA', 'TAG', 'TGA') # create parallel containers that match up codons to aas
    aminos = 'M***' # same as above line
    aas = []
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3] 
        if codon in codons: # first ask if codon is in tuple
            aas.append(aminos[codons.index(codon)]) # asks for codon position in index, retrieve aa from string, append aa to growing protein
        else:
            aas.append('X')
    return ''.join(aas)
'''

'''
sliding window algorithms
general pattern for sliding window
w = 10 # window size
s = 1 # step size
for i in range(0, len(seq) - w + 1, s):
    subseq = seq[i:i+w] # extract window
'''

def gc_comp(seq): # gc composition: proportion of G & C nts in sequence
    return (seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq): # gc skew: measure balance between G and C
    c = seq.count('C')
    g = seq.count('G')
    if c + g == 0: return 0
    return (g-c) / (g+c)




    