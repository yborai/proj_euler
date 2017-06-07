#!/usr/bin/env python3

def is_prime(num):
    for c in range(2, num):
        if num%c == 0:
            return False
    return True

lst = [2]
counter = 3

while not(len(lst) == 10001):
	if is_prime(counter):
		lst.append(counter)
		print(counter)

	counter += 2

print(lst[len(lst)])