#!/usr/bin/env python3
import time
import argparse

def diff_of_sums(num):
	start_time = time.time()
	sosq = 0
	sqos = 0

	for c in range(1, num + 1):
		sosq += c**2
		sqos += c

	print("difference = ", (sqos**2 - sosq))