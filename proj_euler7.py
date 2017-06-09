#!/usr/bin/env python3
import time

def is_prime(num):
    for c in range(2, num):
        if num%c == 0:
            return False
    return True


if __name__ == "__main__":
	start_time = time.time()
	lst = [2]
	counter = 3

	while not(len(lst) == 10001):
		if is_prime(counter):
			lst.append(counter)
			print(counter)

		counter += 2

	print(lst[len(lst)])
	print(time.time() - start_time)