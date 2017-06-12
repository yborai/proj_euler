#!/usr/bin/env python3
import time

def sum_of_primes(n):
<<<<<<< HEAD
    primes = [True]*(n + 1)
    primes[0], primes[1] = [None]*2
    sum = 0
    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False]*(((n)//ind) - 1)
            sum += ind

    return sum
=======
	primes = [True]*(n + 1)
	primes[0], primes[1] = [None]*2
	sum = 0
	for ind, val in enumerate(primes):
		if val is True:
			primes[ind*2::ind] = [False]*(((n)//ind) - 1)
			sum += ind

	return sum
>>>>>>> 9d957983ad66b566d2043c720b6203b4d3de6ef1

if __name__ == "__main__":
    start_time = time.time()

<<<<<<< HEAD
    print(sum_of_primes(2000000))
    print(time.time())
=======
	print(sum_of_primes(2000000))
	print(time.time())
>>>>>>> 9d957983ad66b566d2043c720b6203b4d3de6ef1
