#!/usr/bin/env python3

def num_sundays(start, finish):
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    #num days for each month
	current = (2 + (start - 1900)*365 + 1) % 7
	count = 0
	print(current)

	for c in range(1901, 2000 + 1):
		for val in days:
			if current == 1:
				count += 1

			if(c % 4) == 0 and val == 28 and not((c % 100 == 0) and not(c % 400 == 0)):
				current = (current + 29)%7
			else:
				current = (current + val)%7

	return count






if __name__ == "__main__":
	print(num_sundays(1901, 2000))