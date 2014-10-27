#!/usr/bin/python

# https://projecteuler.net/problem=12

# Answer:


import sys


def triangle_numbers():
    accumulator = 0
    i = 1
    while True:
        accumulator += i
        i += 1
        yield accumulator


def get_factors(n):
    result = set()
    result.add(1)
    result.add(n)
    for i in range(2, n/2 + 1):
        if n % i == 0:
            result.add(i)
            result.add(n/i)
    return result


if __name__ == '__main__':
    n = int(sys.argv[1])
    for t in triangle_numbers():
        count = len(get_factors(t))
        print str(t) + ': %s factors' % count
        if count > n:
            break