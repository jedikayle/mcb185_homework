# 43skew.py by Jedikayle
import sequence

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
    s = seq[i:i+w]
    print(i, sequence.gc_comp(s),sequence.gc_skew(s)) # calls composition and skew functions
 