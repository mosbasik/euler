#!/usr/bin/python

# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

# Answer:
# 232792560
# ./005/005.py 20  6.26s user 0.01s system 99% cpu 6.275 total


import sys


def divisibleByOneToN(number, N):
    for divisor in range(N, 0, -1):
        if (number % divisor != 0):
            return False
        if (divisor == 1):
            return True


def main(N):
    i = N
    while True:
        if divisibleByOneToN(i, N):
            return i
        i += N


if __name__ == '__main__':
    N = int(sys.argv[1])
    print main(N)