# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops


# single loop, with the provided dna sequence
dna = 'ATGGCCTTT'
print('DNA Sequence 1:', dna)

for i in range(0, len(dna)):
    print(i, end=' ')
    print(i % 3, end=' ')
    print(dna[i])

# The interface might be improved for the average user if instead of 'i % 3' we use 'i % 3 + 1', as "reading frame of 0, 1, 2" is better understood as "reading frame of 1, 2, 3"
# Likewise, sequence number should be 'i + 1' to start at "1" instead of "0".
# For the purposes of this class, values begin at 0 for 1, and so on.



# nested loops, with randomized dna sequences of length 9, copied and modified from 22atseq.py

import random
dna = ''

for i in range(0, 9):
    i = random.randint(1,4)
    if i == 1: dna = dna + 'A'
    elif i == 2: dna = dna + 'T'
    elif i == 3: dna = dna + 'C'
    elif i == 4: dna = dna + 'G'

# Uncomment to use the provided dna sequence, for comparison purposes with DNA Sequence 1.
# dna = 'ATGGCCTTT'

print()
print('DNA Sequence 2:', dna)

for i in range(0, len(dna), 3):
    m = i
    step = dna[i:i+3]
    for nt in range(0, len(step), 3):
        print(m + nt, end=' ') 
        print('0', end=' ')
        print(step[nt])
        if len(step) > 1:                   # for variable len(dna), if final step only contains a single nucleotide, Line 42 will be out of range. This if-statement checks this first.
            print(m + nt + 1, end=' ')
            print('1', end=' ')
            print(step[1 + nt])
            if len(step) > 2:               # for variable len(dna), if final step contains (at least one, but) only two nucleotides, Line 46 will be out of range. This if-statement checks this first.
                print(m + nt + 2, end=' ')
                print('2', end=' ')
                print(step[2 + nt])
