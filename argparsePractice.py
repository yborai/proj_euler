#!/usr/bin/env python3

import argparse

def main():
	print("Hello World!")

if __name__ == "__main__":
	main()

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--repeat", action = "store_true")
parser.add_argument("word", type=str)
parser.add_argument("value", type=int)

args = parser.parse_args()

if args.repeat:
	for c in range(args.value):
		print(args.word)