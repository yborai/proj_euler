#!/usr/bin/env python3
import time
<<<<<<< HEAD
import argparse

def diff_of_sums(num):
=======

if __name__ == "__main__":
>>>>>>> 9d957983ad66b566d2043c720b6203b4d3de6ef1
	start_time = time.time()
	sosq = 0
	sqos = 0

<<<<<<< HEAD
	for c in range(1, num + 1):
		sosq += c**2
		sqos += c

	print("difference = ", (sqos**2 - sosq))
=======
	for c in range(1, 101):
		sosq += c**2
		sqos += c

	print("difference = ", (sqos**2 - sosq))
	print(time.time() - start_time)
>>>>>>> 9d957983ad66b566d2043c720b6203b4d3de6ef1
