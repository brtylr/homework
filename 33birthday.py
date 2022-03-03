import sys

def KD(dna):
	sum = 0
	for aa in range(len(dna)):
		if dna[aa] == "R": sum += -4.5
		elif dna[aa] == "K": sum += -3.9
		elif dna[aa] == "N": sum += -3.5
		elif dna[aa] == "D": sum += -3.5
		elif dna[aa] == "Q": sum += -3.5
		elif dna[aa] == "E": sum += -3.5
		elif dna[aa] == "H": sum += -3.2
		elif dna[aa] == "P": sum += -1.6
		elif dna[aa] == "Y": sum += -1.3
		elif dna[aa] == "W": sum += -0.9
		elif dna[aa] == "S": sum += -0.8
		elif dna[aa] == "T": sum += -0.7
		elif dna[aa] == "G": sum += -0.4
		elif dna[aa] == "A": sum += 1.8
		elif dna[aa] == "M": sum += 1.9
		elif dna[aa] == "C": sum += 2.5
		elif dna[aa] == "F": sum += 2.8
		elif dna[aa] == "L": sum += 3.8
		elif dna[aa] == "V": sum += 4.2
		elif dna[aa] == "I": sum += 4.5
		else: print("Invalid aa!")
	return sum/len(dna)

def proline(dna):
	for aa in range(len(dna)):
		if dna[aa] == "P":	return False

seqname = input("Which sequence would you like to run? (e.g. AT1G75120.1): ")
seqnamecheck = " "
toggle1 = 0
toggle2 = 0

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
