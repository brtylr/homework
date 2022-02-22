# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

data = [3, 1, 4, 1, 5]
data.sort()

count = len(data)
sum = 0
dev = 0

for i in range(len(data)):
    sum += data[i]

mean = sum/count

for i in range(len(data)):
    dev += (data[i] - mean) ** 2

if count % 2 == 0: med = ((data[count // 2] + data[(count // 2) - 1]) / 2) #even
else:   med = data[(count // 2)] # odd

print(f'{data}\n{"Count:"} {count}\n{"Minimum:"} {data[0]:.1f}\n{"Maximum:"} {data[count-1]:.1f}\n{"Mean:"} {mean:.3f}\n{"Std. dev:"} {(dev/count)**0.5:.3f}\n{"Median:"} {med:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
