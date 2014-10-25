#!/usr/bin/python

# https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13. What is the 10001st prime number?

# Answer:
# 104743
# ./007.py 10001  0.05s user 0.00s system 98% cpu 0.056 total


import sys
import itertools


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
    N = int(sys.argv[1])
    
    sieve = make_sieve()
    result = 0

    for i in range(N):
        result = sieve.next()

    print result