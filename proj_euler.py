#!/usr/bin/env python3


def is_prime(num):
    for c in range(2, num):
        if num%c == 0:
            return False
    return True


if __name__ == "__main__":
	max = 0
	num = 600851475143

	for c in range(2, num):
	    if is_prime(c):
	        while((num%c) == 0):
	            num = num/c
	            max = c
	            print(c, num)
	        
	print(max)