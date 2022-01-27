#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

# ------

# for those like me who haven't taken calculus in about 10 years:
# a factorial is the running multiple of all integers, beginning from 1, up to integer n
# a factorial looks like n!
# not to be confused with Factorio, an incredibly fun resource-acquisition crafting workflow game
# example: 4! is 4 x 3 x 2 x 1 = 24

n = 5
sum = 0
fac = 1

for i in range(0, n+1):
    sum = i + sum

for i in range(1, n+1):
    fac = i * fac

print (n)
print (sum)
print (fac)