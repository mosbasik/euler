#!/usr/bin/python

# # https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Answer:
# 31875000
# ./009.py 1000  0.04s user 0.01s system 97% cpu 0.049 total


import sys
import math


def get_pythagorean_triplet():
    a = 1
    b = 2
    while True:
        c = math.sqrt(a**2 + b**2)
        if c % 1 == 0:
            yield (a, b, int(c))
        
        if a + 1 != b:
            a += 1
        else:
            a = 1
            b += 1


def find(n):
    for triplet in get_pythagorean_triplet():
        if sum(triplet) == n:
            return triplet[0] * triplet[1] * triplet[2]


if __name__ == '__main__':
    n = int(sys.argv[1])
    print find(n)