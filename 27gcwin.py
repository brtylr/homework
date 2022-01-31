# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops. Instead, count only the first window
# Then 'move' the window by adding 1 letter on one side
# And subtracting 1 letter from the other side
# Describe the pros/cons of this algorith vs. nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
GC = 0

for i in range(0, len(seq)-w+1):
    GC = 0
    print(i, end=' ')
    print(seq[i:i+w], end=' ')
    if seq[i] == 'C' or seq[i] == 'G':
        GC = 1 + GC
    if seq[i+1] == 'C' or seq[i+1] == 'G':
        GC = 1 + GC
    if seq[i+2] == 'C' or seq[i+2] == 'G':
        GC = 1 + GC
    if seq[i+3] == 'C' or seq[i+3] == 'G':
        GC = 1 + GC
    if seq[i+4] == 'C' or seq[i+4] == 'G':
        GC = 1 + GC
    if seq[i+5] == 'C' or seq[i+5] == 'G':
        GC = 1 + GC
    if seq[i+6] == 'C' or seq[i+6] == 'G':
        GC = 1 + GC
    if seq[i+7] == 'C' or seq[i+7] == 'G':
        GC = 1 + GC
    if seq[i+8] == 'C' or seq[i+8] == 'G':
        GC = 1 + GC
    if seq[i+9] == 'C' or seq[i+9] == 'G':
        GC = 1 + GC
    if seq[i+10] == 'C' or seq[i+10] == 'G':
        GC = 1 + GC
    print('%.4f' % (GC / w))

# As opposed to nested loops, this program functions but it is tedious to write out due to its length.
# It is also very hard to re-code as a change in 'w' requires a manual extension/shortening of all the if-statements.
# For large values of 'w', say w = 1000, this would be incredibly impractical.
# Furthermore, this would not work well with a 'w' that varies, as the code would need to be changed every single time.
# The only real pro is that it may be more clear with the breakdown of each if-statement what exactly is happening at each line.
# And furthmore, if there was a need to exclude certain values from each window's GC calculation, e.g. the first and last nucleotides, then one could simply erase 'seq[i]' and 'seq[i+10]' (generalized: 'seq[i+w-1]').
