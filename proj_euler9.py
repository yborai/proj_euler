#!/usr/bin/env python3

def rank(hand, values):
	temp = []
	refined = []
	multiplicity = dict()
	s_flag = False
	f_flag = False


	for c in range(5):
		temp.append(values.index(hand[int(3*c):int(1 + 3*c)]))

	temp.sort()

	for c in range(5):
		refined.append(values[temp[c]])

	for c in range(1, 5):
		print()

		if refined[c] in multiplicity:
			multiplicity[refined[c]] = 1
		else:
			multiplicity[refined[c]] += 1

	print(multiplicity)
			


values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
P1wins = 0
P2wins = 0
priority1 = 0
priority2 = 0



with open('poker.textile', 'r') as f:
	content = f.readlines()

print(content[0])

for c in range(len(content)):
	priority1 = rank(content[c][:15], values)
	priority2 = rank(content[c][15:], values)

