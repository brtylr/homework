import sys

aa = ("R", "K", "N", "D", "Q", "E", "H", "P", "Y", "W", "S", "T", "G", "A", "M", "C", "F", "L", "V", "I")
hydropathy = (-4.5, -3.9, -3.5, -3.5, -3.5, -3.5, -3.2, -1.6, -1.3, -0.9, -0.8, -0.7, -0.4, 1.8, 1.9, 2.5, 2.8, 3.8, 4.2, 4.5)
seqname = input("Which sequence would you like to run? (e.g. AT1G75120.1): ")
seqnamecheck = " "
toggle1 = 0
toggle2 = 0

def KD(dna):
	sum = 0
	for i in range(len(dna)):
		for j in range(20):
			if dna[i] == aa[j]: sum += hydropathy[j]
		
	return sum/len(dna)

def proline(dna):
	for aa in range(len(dna)):
		if dna[aa] == "P":	return False
		
with open(sys.argv[1]) as fp:
	seq = "0"
	while seqname != seqnamecheck:
		line = fp.readline()
		seqnamecheck = line[1:len(seqname)+1]
	else:
		while seq == "0" or seq[len(seq)-2] != "*":
			seq = seq[0:len(seq)-1]
			seq += fp.readline()

print(f'\n{line}\n{seq}')

for i in range(22):
	sigpep = seq[i:i+8]
	if KD(sigpep) > 2.5:
		print(f'{"Suspected signal peptide "}{sigpep}{" with KD = "}{KD(sigpep):.2f}{" found at position "}{i+1}{"."}')
		toggle1 = 1
		break

if toggle1 == 0:	print(f'{"Presence of a signal peptide is unlikely. No average value of KD > 2.5 found for an 8-amino acid length sequence within first 30 amino acids."}')


for i in range(30, len(seq)-12):
	phobicity = seq[i:i+11]
	if KD(phobicity) > 2.0:
		if proline(phobicity) == False:	break
		print(f'{"Suspected hydrophobic region "}{phobicity}{" with KD = "}{KD(phobicity):.2f}{" found at position "}{i+1}{". No prolines are present in region."}')
		toggle2 = 1
		break

if toggle2 == 0:	print(f'{"Presence of a hydrophobic region is unlikely. No average value of KD > 2.0 found for an 11-amino acid length sequence past the first 30 amino acids."}')

if toggle1 == 0 or toggle2 == 0:	print(f'\n{"Conditions are NOT met for a trans-membrane protein."}\n')
else:	print(f'\n{"Conditions HAVE been met for a suspected trans-membrane protein."}\n')
