#!/usr/bin/env python3

def rank(hand, values):
	temp = []
	refined = []
	multiplicity = dict()
	counter = 1
	rank = 0

	s_flag = False
	f_flag = False


	for c in range(5):
		temp.append(values.index(hand[int(3*c):int(1 + 3*c)]))

	temp.sort()

	for c in range(5):
		refined.append(values[temp[c]])

	for c in range(1, 5):
		if not(refined[c] == refined[c - 1]):
			multiplicity[refined[c - 1]] = counter
			counter = 1
		else:
			counter += 1

		if c == 4:
			multiplicity[refined[c]] = counter

	if(2 in list(multiplicity.values())):
		rank = 1

	if(2 in list(multiplicity.values())) and (len(multiplicity.values()) == 3):
		rank = 2

	if(3 in list(multiplicity.values())):
		rank = 3

	if(temp[4] == (temp[3] + 1) == (temp[2] + 2) == (temp[1] + 3) == (temp[0] + 4)):
		s_flag = True
		rank = 4

	print(hand[1:2], hand[4:5], hand[7:8], hand[10:11], hand[13:14])
	if(hand[1:2] == hand[4:5] == hand[7:8] == hand[10:11] == hand[13:14]):
		f_flag = True
		rank = 5	

	if(3 in list(multiplicity.values())) and (2 in list(multiplicity.values())):
		rank = 6

	if(4 in list(multiplicity.values())):
		rank = 7

	if(s_flag == True) and (f_flag == True):
		rank = 8

		if(temp[4] == 12):
			rank = 9

	return (rank, temp)



values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
P1wins = 0
P2wins = 0
priority1 = 0
priority2 = 0
order1 = []
order2 = []



with open('poker.textile', 'r') as f:
	content = f.readlines()

print(content[0])

for c in range(len(content)):
	priority1, order1 = rank(content[c][:15], values)
	priority2, order2 = rank(content[c][15:], values)
	print(priority1, priority2)

	if (priority1 > priority2):
		P1wins += 1
	elif (priority2 < priority1):
		P2wins += 1 
	else:
		for c in range(4, -1, -1):
			if (order1[c] > order2[c]):
				P1wins += 1
				break
			elif (order1[c] < order2[c]):
				P2wins += 1
				break

print(P1wins, P2wins)

