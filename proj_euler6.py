#!/usr/bin/env python3

sosq = 0
sqos = 0

for c in range(1, 101):
	sosq += c**2
	sqos += c

print("difference = ", (sqos**2 - sosq))