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
