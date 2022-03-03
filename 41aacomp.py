import sys

aa = ("A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y")
count = [0] * 20
freq = [0] * 20

with open(sys.argv[1]) as fp:
	seq = "0"
	for line in fp.readlines():
		if line[0] != ">":
			if seq == "0" or line[len(line)-2] != "*": seq += line[0:len(line)-1]
			else: seq += line[0:len(line)-2]

for i in range(len(seq)):
	for j in range(20):
		if seq[i] == aa[j]: count[j] += 1

for i in range(20):
	freq[i] = count[i]/sum(count)
	print(f'{aa[i]}\t{count[i]}\t{freq[i]}')
