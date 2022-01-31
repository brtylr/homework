# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
GC = 0

for i in range(0, len(seq)-w+1):
    GC = 0
    win = seq[i:i+w]
    print(i, end=' ')
    print(seq[i:i+w], end=' ')
    for i in range(0, len(win)):
        if win[i] == 'G' or win[i] == 'C':
            GC = 1 + GC
    print('%.4f' % (GC / w))
