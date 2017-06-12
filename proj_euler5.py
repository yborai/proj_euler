#!/usr/bin/env python3
import time

if __name__ == "__main__":
	start_time = time.time()
	min = 20
	flag = False

	for c in range(2520, 1000000000, 20):
		for n in range(20, 0, -1):
			if not(c%n == 0):
				if n < min:
					min = n

				print(n)
				break

			if n == 1:
				flag = True
				print('c*n=', c*n)

		if flag == True:
			break

	print(min)
	print(time.time() - start_time)
