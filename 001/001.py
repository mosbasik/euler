#!/usr/bin/python

# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all
# the multiples of 3 or 5 below 1000.


def multiples_of_3_or_5(N):
    '''
    Given an integer N, find all the multiples of 3 or 5 on [0, N).
    '''
    return [x for x in range(N) if (x % 3 == 0) or (x % 5 == 0)]


if __name__ == '__main__':
    print sum(multiples_of_3_or_5(1000))