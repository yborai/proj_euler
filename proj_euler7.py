#!/usr/bin/env python3
import time

def is_prime(num):
    for c in range(2, num):
        if num%c == 0:
            return False
    return True


def n_prime(n):
	primes = [True]*10000000
	primes[0], primes[1] = [None]*2
	count=0

	for ind, val in enumerate(primes):
		if val == True:
			if len(primes[ind*2::ind]) == len([False]*((10000000//ind) - 1)):
				primes[ind*2::ind] = [False]*((10000000//ind)- 1)
			else:
				primes[ind*2::ind] = [False]*((10000000//ind)- 2)

			count+=1

		if count == n:
			return(count)

	return(count)


