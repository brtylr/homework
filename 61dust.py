#!/usr/bin/env python3
# 61dust.py

import mcb185 as mcb
import argparse

# parser setup
duster = argparse.ArgumentParser(description='Hard-mask a sequence with Ns or soft-mask with lowercase nucleotides, using a Shannon entropy threshold.')

duster.add_argument('--file', required=True, type=str,
	metavar='<str>', help='Sequence FASTA file')
duster.add_argument('--size', required=False, type=int, default=4,
	metavar='<int>', help='Window size. Default = [%(default)s]')
duster.add_argument('--level', required=False, type=int, default=0,
	metavar='<int>', help='Mask level, hard-mask = 0 and soft-mask = 1. Default = [%(default)s]')
duster.add_argument('--threshold', required=False, type=float, default=1.6,
	metavar='<float>', help='Entropy threshold. Default = [%(default)s]')

arg = duster.parse_args()

#read fasta file
sequence = ""

for name, seq in mcb.read_fasta(arg.file):
	sequence = seq

#DUST sequencing
print(mcb.dust_masker(sequence, arg.size, arg.level, arg.threshold))
