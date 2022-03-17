import re
import sys

file = sys.argv[1]
restrictpat = sys.argv[2]
trigger = "ORIGIN"
toggle1 = False
seq = ""
matchvalue = 0

with open(file) as fp:
	for line in fp.readlines():
		if trigger in line and toggle1 == False:		
			toggle1 = True
		elif toggle1 == True and line[0:1] != "//":
			words = line.split()
			seq += "".join(words[1:])
			
for match in re.finditer(restrictpat, seq):
	print(match.start()-matchvalue)
	matchvalue =  match.start()	
