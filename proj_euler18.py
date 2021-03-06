#!/usr/bin/env python3
import argparse 
import time

def max_path_sum(pyramid, number):
    for c in range(len(pyramid[number])):  #replaces current row with the max addition of the terms below it
        pyramid[number][c] += max([pyramid[number + 1][c], pyramid[number + 1][c + 1]])


    if len(pyramid[number]) == 1: #exits at top of pyramid
        return pyramid[number][0]
    else:
        return max_path_sum(pyramid, number - 1)   #moves up a row

if __name__ == "__main__":
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type = str)

    pyramid = []
    args = parser.parse_args()
    stuff = ""

    if args.file == None:
        with open("triangle.txt", 'r') as f:
            stuff = f.readlines()
    else:
        with open(args.file, 'r') as f:
            stuff = f.readlines()

    for c in stuff:
        pyramid.append([int(i) for i in c.split()])

    print(pyramid)
    print(max_path_sum(pyramid,len(pyramid) - 2))
    print((time.time() - start_time), 'seconds')