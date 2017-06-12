#!/usr/bin/env python3


def ind_combs(coins, pos):
	keys = list(coins.keys())
	num = 0

	if pos == 0:
		return

	print(coins[keys[pos]][0])
	while not(num >= (coins[keys[pos]])[0]):
		if (num + coins[keys[pos - 1]][0]) > num:
			coins[keys[pos]][1] += coins[keys[pos - 2]][1]
			num += coins[keys[pos - 2]][0]
		else:
			print(num)
			coins[keys[pos]][1] += coins[guy[pos - 1]][1]
			num += coins[keys[pos - 1]][0]



def poss_combs(coins):
    for c in range(len(coins.keys())):
    	ind_combs(coins, c)

    return 



if __name__ == "__main__":
	coins = {0 : [1, 0], 1 : [2, 1], 2 : [5, 0], 3 : [10, 0], 4 : [20, 0], 5: [50, 0], 6 : [100, 0], 7 : [200, 0]}

	poss_combs(coins)
	print(coins)