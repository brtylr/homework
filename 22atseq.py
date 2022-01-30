from multiprocessing.context import assert_spawning
import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# dna = ''
# not needed as 'dna' is defined in loop

AT = 0
# pre-defined for initial while condition

while not AT / 30 == 0.6:
    AT = 0
    dna = ''
    # both 'AT' and 'dna' reset as zero, or else they will grow indefinitely in loop
    for i in range(0, 30):
        i = random.randint(1,4)
        if i == 1:
            dna = dna + 'A'
            AT += 1
        elif i == 2:
            dna = dna + 'T'
            AT += 1
        elif i == 3:
            dna = dna + 'C'
        elif i == 4:
            dna = dna + 'G'

# loop breaks when 60% AT is reached

print('Sequence length:', len(dna))
print('AT% content:', end=' ')
print('%.2f' %  (AT / len(dna)))
print('Sequence:', dna)

# this is an alternative method of ensuring AT average is 60%, by forcing it to be 60%
