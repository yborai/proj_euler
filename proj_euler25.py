#!/usr/bin/env python3
def fib_term(dig):
	memo = {1 : 1, 2 : 1}

	for c in range(3, 100000000):
		memo[c] = memo[c - 1] + memo[c - 2]
		if len(str(memo[c])) == dig:
			return c

if __name__ == "__main__":
	print(fib_term(1000))