# 35scoringmatrix.py by Jedikayle
import sys

nts = sys.argv[1] # nucleotide alph ACGT
matches = sys.argv[2] # match score
mismatches = sys.argv[3] # mismatch score

print('   ', end = '')	# ' ' gap top left corner of the matrix.

for nt in nts:	# loop will print each nucleotide from nts list
	print(nt, end = '  ') # end=' ' space after each nucleotide, does not go to next line
print()	# move to next line

for ntrows in nts:	
	print(ntrows, end = ' ') # print nts in each row followed by a space
	for ntcols in nts:
		if ntrows == ntcols: print(matches, end = ' ') # if two nts match, then will print the matches CLA
		else: print(mismatches, end =' ') # if two nts do not match, will print the mismatches CLA
	print()