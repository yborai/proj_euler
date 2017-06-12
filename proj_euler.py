#!/usr/bin/env python3


def is_prime(num):
    for c in range(2, num):
        if num%c == 0:
            return False
    return True


<<<<<<< HEAD
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
=======
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
>>>>>>> 9d957983ad66b566d2043c720b6203b4d3de6ef1
