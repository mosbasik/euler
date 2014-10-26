#!/usr/bin/python

# https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Answer:
# 142913828922
# ./010.py 2000000  0.97s user 0.02s system 99% cpu 0.986 total


import itertools
import sys


def make_sieve():

    # dictionary where the keys are all composite numbers and the values are the
    # corresponding first-found prime factors of those composite numbers
    D = {}

    # q is 2, 3, 4, 5, ...  (all integers greater than 1)
    for q in itertools.count(2):

        p = D.pop(q, None)

        if p is None:
            yield q     # q is not a key in D, therefore q is prime
            D[q*q] = q  # the square of q is certainly composite, so put it in D

        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p



if __name__ == '__main__':
    n = int(sys.argv[1])
    result = 0
    for prime in make_sieve():
        if prime < n:
            result += prime
            continue
        break
    print result