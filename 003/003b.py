#!/usr/bin/python

# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import sys

def greatestPrimeFactor(N):
    prime = -1
    i = 1
    cap = N
    while (i < cap):
        if (N % i == 0):
            cap = N / i
            n = 1
            while (n <= i+1):
                if (n > 1):
                    if (i == n):
                        prime = i 
                        break 
                    elif (i % n == 0):
                        break
                n += 1
        i += 1
    return prime


if __name__ == '__main__':
    n = int(sys.argv[1])
    print "%d's greatest prime factor: %d" % (n, greatestPrimeFactor(n))