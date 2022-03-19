import mcb185 as mcb
import argparse

# Parser for program input
orfer = argparse.ArgumentParser(description='Sequence 3-frame or 6-frame translations to find the longest open reading frame within precursor mRNA.')

orfer.add_argument('--file', required=True, type=str,
	metavar='<str>', help='Sequence FASTA file')
orfer.add_argument('--frameswitch', action='store_true',
	help='Switch from 3-frame (forward) to 6-frame (forward & reverse) translation')

arg = orfer.parse_args()

sequence = ""

# Read file, produce forward peptide sequence, and reverse peptide sequence if switch is on
for name, dna_sequence in mcb.read_fasta(arg.file):
	if arg.frameswitch:
		reverse_seq = mcb.complementary_DNA(dna_sequence)
		forward_pep = mcb.translation(mcb.RNA_converter(dna_sequence))
		reverse_pep = mcb.translation(mcb.RNA_converter(reverse_seq))
	else:
		forward_pep = mcb.translation(mcb.RNA_converter(dna_sequence))

# Check for start and stop codons
max_size = 0

for i in range(len(forward_pep)):
	if forward_pep[i] == "M":
		for j in range(i, len(forward_pep)):
			if forward_pep[j] == "X":
				if (j-i+1) >= max_size:
					max_size = j - i + 1
					longest_orf = forward_pep[i:j+1]
					break
				else:	break

if arg.frameswitch:
	for i in range(len(reverse_pep)):
		if reverse_pep[i] == "M":
			for j in range(i, len(reverse_pep)):
				if reverse_pep[j] == "X":
					if (j-i+1) >= max_size:
						max_size = j - i + 1
						longest_orf = reverse_pep[i:j+1]
						break
					else:	break

# Print longest ORF and size
print(longest_orf, max_size)
