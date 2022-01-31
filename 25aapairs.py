# Print out all the unique pairwise amino acid combinations
# AC is the same as CA
# Skip AA, CC etc.
# Also print out how many combinations there are

# AAs: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y

aa = 'ACDEFGHIKLMNPQRSTVWY'
t = 0 

for i in range(0, len(aa)):
    O = aa[i]
    m = 1 + i
    s = 0
    for i in range(0, len(aa)):
        P = aa[i]
        n = 1 + i
        if not O == P and n > m: # if O = P, AAs are the same; if n > m, O & P are in alphabetical order, thus cannot repeat in reverse order
            print(O, P)
            s = 1 + s
    t = t + s

print('# of AA combinations:', t)
