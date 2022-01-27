dna = 'ATAGCGAATATCTCTCATGAGAGGGAAD'

# k = return sequence length, which is 3 for codons, but can be changed to be any value to allow the code to run.
# The only drawback is that dna sequence length must be divisible by k, or else remaining values will not be shown.

k = 3

for i in range(0, len(dna)-k+1, k):
	print(dna[i:i+k])