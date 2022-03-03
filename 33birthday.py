# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random
#on = 1
#bmonth = []
#bday = []
#birth = []
#name = []
shared = 0

"""
python3 33birthday.py
0.571
"""

#while on == 1:
#	bmonth.append(int(input("Please enter month of birth in MM format (e.g. 07): ")))
#	bday.append(int(input("Please enter day of birth in DD format (e.g. 15): ")))
#	name.append(input("Give this person a name: "))	
#	birth.append(random.randint(0, 364))
#	check = input("Would you like to add another person? [Y/n?] ")
#	if check == "Y" or check == "y":	on = 1
#	else:	on = 0

cal = [0] * 365
trials = int(input("How many people would you like to run? "))

for i in range(trials):
	cal[random.randint(0, 364)] += 1
#	birth.append(random.randint(0, 364))
	
for i in range(len(cal)):
	if cal[i] > 1:	shared += 1

print(f'{shared/trials:.3f}')
