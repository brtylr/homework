# mcb185.py

import sys
import gzip
import math

def read_fasta(filename):
	name = None
	seqs = []

	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

# Shannon entropy calculator, -sum(p * log2(p))

def shannon_entropy(seq):
	ntlist = [0, 0, 0, 0] #[A, C, G, T]
	entropy_sum = 0.0
	for i in range(len(seq)):
		if seq[i] == "A" or seq[i] ==  "a":	ntlist[0] += 1
		elif seq[i] == "C" or seq[i] ==  "c":	ntlist[1] += 1
		elif seq[i] == "G" or seq[i] ==  "g":	ntlist[2] += 1
		elif seq[i] == "T" or seq[i] ==  "t":	ntlist[3] += 1
	for i in range(len(ntlist)):
		if ntlist[i] == 0:	continue
		else:	entropy_sum += -((ntlist[i]/len(seq))*(math.log2(ntlist[i]/len(seq))))
	return entropy_sum	

# Must a sequence using DUST. seq = sequence, window_size = sequencing window, mask_level = 0 is hard mask (N), mask_level = 1 is soft mask (lowercase acgt), threshold is Shannon entropy threshold
def dust_masker(seq, window_size, mask_level, threshold):
	seq_list = ["0"] * len(seq)
	for i in range(0, len(seq)-window_size+1):
		window = seq[i:i+window_size]
		if shannon_entropy(window) <= threshold:
			if mask_level == 0:
				for nt in range(len(window)):
					seq_list[i+nt] = "N"
			elif mask_level == 1:
				for nt in range(len(window)):
					if seq_list[i+nt] != "0": continue
					else:
						if window[nt] == "A" or window[nt] ==  "a":	seq_list[i+nt] = "a"
						elif window[nt] == "C" or window[nt] ==  "c":	seq_list[i+nt] = "c"
						elif window[nt] == "G" or window[nt] ==  "g":	seq_list[i+nt] = "g"
						elif window[nt] == "T" or window[nt] ==  "t":	seq_list[i+nt] = "t"
		else:
			for nt in range(len(window)):
				if seq_list[i+nt] == "N" or seq_list[i+nt] == "a" or seq_list[i+nt] =="c" or seq_list[i+nt] =="g" or seq_list[i+nt] =="t": continue
				elif seq_list[i+nt] == "0":
					if window[nt] == "A" or window[nt] == "a": seq_list[i+nt] = "A"
					elif window[nt] == "C" or window[nt] == "c": seq_list[i+nt] = "C"
					elif window[nt] == "G" or window[nt] == "g": seq_list[i+nt] = "G"
					elif window[nt] == "T" or window[nt] == "t": seq_list[i+nt] = "T"
					else:	seq_list[i+nt] = window[nt]
	mask_sequence = "".join(seq_list)
	return(mask_sequence)

# DNA to RNA converter
def RNA_converter(dna_seq):
	rna_seq = [0] * len(dna_seq)
	for i in range(len(dna_seq)):
		if dna_seq[i] == "A" or dna_seq[i] == "a":	rna_seq[i] = "A"
		elif dna_seq[i] == "C" or dna_seq[i] == "c":	rna_seq[i] = "C"
		elif dna_seq[i] == "G" or dna_seq[i] == "g":	rna_seq[i] = "G"
		elif dna_seq[i] == "T" or dna_seq[i] == "t":	rna_seq[i] = "U"
	rna_seq = "".join(rna_seq)
	return rna_seq

# DNA to complementary DNA converter
def complementary_DNA(dna_seq):
	comp_dna = []
	for i in range(len(dna_seq)-1, -1, -1):
		comp_dna.append(dna_seq[i])
	comp_dna = "".join(comp_dna)
	return comp_dna


# RNA translation to amino acid
def translation(rna):
	rna_seq = rna	# Preserves original rna string

	if len(rna_seq)%3 == 1:	rna_seq = rna_seq[0:len(rna_seq)-1]		# Removes remainder of 1 from translation
	elif len(rna_seq)%3 == 2:	rna_seq = rna_seq[0:len(rna_seq)-2]	# Removes remainder of 2 from translation

	pep_seq = [0] * int((len(rna_seq)/3))

	for i in range(0, len(rna_seq), 3):		# Amino acid translating loop
		if rna_seq[i] == "U":
			if rna_seq[i+1] == "U":	#U _ _
				if rna_seq[i+2] == "U":	pep_seq[int(i/3)] = "F"
				elif rna_seq[i+2] == "C":	pep_seq[int(i/3)] = "F"
				elif rna_seq[i+2] == "A":	pep_seq[int(i/3)] = "L"
				elif rna_seq[i+2] == "G":	pep_seq[int(i/3)] = "L"
			elif rna_seq[i+1] == "C":	pep_seq[int(i/3)] = "S"
			elif rna_seq[i+1] == "A":
				if rna_seq[i+2] == "U":	pep_seq[int(i/3)] = "Y"
				elif rna_seq[i+2] == "C":	pep_seq[int(i/3)] = "Y"
				elif rna_seq[i+2] == "A":	pep_seq[int(i/3)] = "X"
				elif rna_seq[i+2] == "G":	pep_seq[int(i/3)] = "X"
			elif rna_seq[i+1] == "G":
				if rna_seq[i+2] == "U":	pep_seq[int(i/3)] = "C"
				elif rna_seq[i+2] == "C":	pep_seq[int(i/3)] = "C"
				elif rna_seq[i+2] == "A":	pep_seq[int(i/3)] = "X"
				elif rna_seq[i+2] == "G":	pep_seq[int(i/3)] = "W"
		elif rna_seq[i] == "C":	#C _ _
			if rna_seq[i+1] == "U":	pep_seq[int(i/3)] = "L"
			elif rna_seq[i+1] == "C":	pep_seq[int(i/3)] = "P"
			elif rna_seq[i+1] == "A":
				if rna_seq[i+2] == "U":	pep_seq[int(i/3)] = "H"
				elif rna_seq[i+2] == "C":	pep_seq[int(i/3)] = "H"
				elif rna_seq[i+2] == "A":	pep_seq[int(i/3)] = "Q"
				elif rna_seq[i+2] == "G":	pep_seq[int(i/3)] = "Q"
			elif rna_seq[i+1] == "G":	pep_seq[int(i/3)] = "R"
		elif rna_seq[i] == "A":	#A _ _
			if rna_seq[i+1] == "U":	
				if rna_seq[i+2] == "U":	pep_seq[int(i/3)] = "I"
				elif rna_seq[i+2] == "C":	pep_seq[int(i/3)] = "I"
				elif rna_seq[i+2] == "A":	pep_seq[int(i/3)] = "I"
				elif rna_seq[i+2] == "G":	pep_seq[int(i/3)] = "M"
			elif rna_seq[i+1] == "C":	pep_seq[int(i/3)] = "T"
			elif rna_seq[i+1] == "A":
				if rna_seq[i+2] == "U":	pep_seq[int(i/3)] = "N"
				elif rna_seq[i+2] == "C":	pep_seq[int(i/3)] = "N"
				elif rna_seq[i+2] == "A":	pep_seq[int(i/3)] = "K"
				elif rna_seq[i+2] == "G":	pep_seq[int(i/3)] = "K"
			elif rna_seq[i+1] == "G":
				if rna_seq[i+2] == "U":	pep_seq[int(i/3)] = "S"
				elif rna_seq[i+2] == "C":	pep_seq[int(i/3)] = "S"
				elif rna_seq[i+2] == "A":	pep_seq[int(i/3)] = "R"
				elif rna_seq[i+2] == "G":	pep_seq[int(i/3)] = "R"
		elif rna_seq[i] == "G":	#G _ _
			if rna_seq[i+1] == "U":	pep_seq[int(i/3)] = "V"
			elif rna_seq[i+1] == "C":	pep_seq[int(i/3)] = "A"
			elif rna_seq[i+1] == "A":
				if rna_seq[i+2] == "U":	pep_seq[int(i/3)] = "D"
				elif rna_seq[i+2] == "C":	pep_seq[int(i/3)] = "D"
				elif rna_seq[i+2] == "A":	pep_seq[int(i/3)] = "E"
				elif rna_seq[i+2] == "G":	pep_seq[int(i/3)] = "E"
			elif rna_seq[i+1] == "G":	pep_seq[int(i/3)] = "G"

	pep_seq = "".join(pep_seq)
	return pep_seq
