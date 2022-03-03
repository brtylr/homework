# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""

import math
import sys

sum = 0
prob = []

for i in range(1, len(sys.argv)):
	prob.append(float(sys.argv[i]))

print(prob)

for i in range(len(prob)):
	sum -= prob[i] * (math.log2(prob[i]))

print(sum)
