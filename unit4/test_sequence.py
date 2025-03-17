# test_sequence.py by Jedikayle
import sequence # using sequence library that was created

print(sequence.transcribe('ACGT'))
print(sequence.revcomp('AAAACGT'))
print(sequence.translate('ATGCCCTAA'))

s = 'ACGTGGGGGGCATATG'
print(sequence.gc_comp(s))
print(sequence.gc_skew(s), sequence.gc_skew(sequence.revcomp(s)))