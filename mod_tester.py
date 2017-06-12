#!/usr/bin/env python3

import argparse
from proj_euler import prime_time
from proj_euler7 import n_prime
from proj_euler6 import diff_of_sums
from proj_euler8 import big_guy
from proj_euler9 import rank
from proj_euler10 import sum_of_primes

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--prime", action = "store_true")
parser.add_argument("-s", "--sums", action = "store_true")
parser.add_argument("-n", "--nth", action = "store_true")
parser.add_argument("-b", "--big", action = "store_true")
parser.add_argument("-d", "--sop", action = "store_true")
parser.add_argument("-r", "--rank", action = "store_true")

args = parser.parse_args()

max = 0

if not(args.prime):
	prime_time(600851475143)
	diff_of_sums(100)
	n_prime(10001)
	big_guy()
	print(sum_of_primes(2000000))
