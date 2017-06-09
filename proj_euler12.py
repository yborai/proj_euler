#!/usr/bin/env python3
from functools import reduce

def hdtn(num):
	cur_tn = 0
	for c in range(1, 10000000):
		print(cur_tn)
		cur_tn += c
		if len(set(reduce(list.__add__, ([i, cur_tn//i] for i in range(1, int(cur_tn**0.5) + 1) if cur_tn % i == 0)))) > num:
		    return(cur_tn) 

if __name__ == "__main__":
	print(hdtn(500))