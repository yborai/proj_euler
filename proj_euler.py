#!/usr/bin/env python3


def is_prime(num):
    for c in range(2, num):
        if num%c == 0:
            return False
    return True


def prime_time(num):
	max = 0

	for c in range(2, num):
	    if is_prime(c):
	        while((num%c) == 0) and not(num == 1):
	            num = num/c
	            max = c
	            if(num == 1):
	            	print(max)
	            	return(max)