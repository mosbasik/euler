#!/usr/bin/python

# # https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Answer:


import sys
import math


def get_pythagorean_triplet(a=1, b=2):
    while True:
        c = math.sqrt(a**2 + b**2)
        # print str(a) + ' ' + str(b) + ' ' + str(c)

        if c % 1 == 0:
            yield (a, b, int(c))

            if a+1 == b:
                a = 1
                b += 1

            else:
                a += 1
        
        elif a+1 == b:
            for trip in get_pythagorean_triplet(1, b+1):
                yield trip

        else:
            for trip in get_pythagorean_triplet(a+1, b):
                yield trip


if __name__ == '__main__':
    n = int(sys.argv[1])
    p = get_pythagorean_triplet()
    for i in range(n):
        print next(p)