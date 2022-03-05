import sys
kmer = []
kcount = []
ksize = int(sys.argv[2])
file = sys.argv[1]
nuc1 = ""
seq = ""

def nucleotide(n):
	global nuc1
	nt = ["A", "C", "G", "T"]
	if n == 0:
		kmer.append(nuc1)
		kcount.append(0)
	else:
		for i in range(len(nt)):	
			nuc1 += nt[i]
			nucleotide(n-1)
			nuc1 = nuc1[0:len(nuc1)-1]

nucleotide(ksize)

with open(file) as fp:
	for line in fp.readlines():
		if line[0] == ">": continue
		else: seq += line[0:len(line)-1]
	
for i in range(0, len(seq)-ksize+1):
	for j in range(len(kmer)):
		if seq[i:i+ksize] == kmer[j]:
			kcount[j] += 1
			break
		
print(f'{"k-mer"}\t{"Count"}\t{"Frequency"}')

for i in range(len(kmer)):
	print(f'{kmer[i]}\t{kcount[i]}\t{kcount[i]/sum(kcount):.4f}')
