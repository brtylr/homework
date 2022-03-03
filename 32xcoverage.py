#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""

data = [0] * int(sys.argv[1])
sum = 0

for i in range(int(sys.argv[2])):
	j = random.randint(0, (int(sys.argv[1]) - (int(sys.argv[3]) + 1)))
	k = j + (int(sys.argv[3])) - 1
	for x in range(j, k):
		data[x] += 1
	
data.sort()

for i in range(int(sys.argv[1])):
	sum += int(data[i])

print(f'{"Minimum:"} {data[0]}\n{"Maximum:"} {data[int(sys.argv[1])-1]}\n{"Average:"} {sum/int(sys.argv[1])}')
