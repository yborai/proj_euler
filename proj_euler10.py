#!/usr/bin/env python3
import time

def sum_of_primes(n):
    primes = [True]*(n + 1)
    primes[0], primes[1] = [None]*2
    sum = 0
    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False]*(((n)//ind) - 1)
            sum += ind

    return sum

if __name__ == "__main__":
    start_time = time.time()

    print(sum_of_primes(2000000))
    print(time.time())

