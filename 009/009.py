#!/usr/bin/python

# # https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Answer:


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


if __name__ == '__main__':
    n = int(sys.argv[1])
    p = get_pythagorean_triplet()
    for i in range(n):
        print next(p)