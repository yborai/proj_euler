#!/usr/bin/env python3

def ap(l_bound, u_bound, num):
	mid = int((u_bound + l_bound) / 2)
	print(mid)
	print(mid/num)
	print(round(((mid / num) * ((mid - 1) / (num - 1))), 12))
	if round(((mid / num) * ((mid - 1) / (num - 1))), 12) > (1 / 2):
		return ap(l_bound, mid, num)
	elif round(((mid / num) * ((mid - 1) / (num - 1))), 12) < (1 / 2):
		return ap(mid, u_bound, num)
	else:
		return mid

if __name__ == "__main__":
	print(ap(0, 10**12, 10**12))