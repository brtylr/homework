import random

# DNA randomizer copied and modified from 22atseq.py

dna = ''

for i in range(0, 30):
    i = random.randint(1,4)
    if i == 1: dna = dna + 'A'
    elif i == 2: dna = dna + 'T'
    elif i == 3: dna = dna + 'C'
    elif i == 4: dna = dna + 'G'

rev = ''

for i in range(len(dna)-1, -1, -1):
    if dna[i] == 'A': rev = rev + 'T'
    elif dna[i] == 'T': rev = rev + 'A'
    elif dna[i] == 'C': rev = rev + 'G'
    elif dna[i] == 'G': rev = rev + 'C'

print('DNA Sequence:', dna)
print('Reverse Complement:', rev)
