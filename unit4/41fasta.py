# 41fasta.py

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline[:30], seq[:40], len(seq))
