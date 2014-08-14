#!/usr/bin/python

# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


import sys
import math


def isPrime(N):
    if N <= 1: return 0
    i = 2
    while (i * i <= N):
        if (N % i == 0):
            return 0
        i +=1
    return 1


def greatestPrimeFactor(N):
    rootN = int(math.ceil(math.sqrt(N)))
    for i in range(rootN, 1, -1):
        print i
        if (N % i == 0):
            if isPrime(i):
                return i
    assert(False)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print "is %d prime? %d" % (n, isPrime(n))
    print "%d's greatest prime factor: %d" % (n, greatestPrimeFactor(n))