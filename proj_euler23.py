#!/usr/bin/env python3
from functools import reduce
import time

def get_factors(num):
	return [
		[i, num//i]
		for i in range(1, int(num**0.5) + 1)
		if num % i == 0
	]

def is_abundant(num): 
	dude = set(reduce(
		list.__add__,
		get_factors(num)
	))
	if (sum(dude) - num) > num:
		return True
	else:
		return False

def is_sum(num, guy):
	for val in guy:
		if val > (num / 2):
			return False

		if (num - val) in guy:
			print(num)
			return True

	return False

if __name__ == "__main__":
	start_time = time.time()
	guy = []
	total = 0
	
	for n in range(12, 28123): 
		if is_abundant(n):
			guy.append(n)

	print(guy) 

	for c in range(20161 + 1):
		if not is_sum(c, guy):
			total += c

	print(total)
	print((time.time() - start_time), 'seconds')
