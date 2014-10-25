#!/usr/bin/python

# https://projecteuler.net/problem=8
# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 * 9 * 8 * 9 = 5832. Find the thirteen adjacent digits in the
# 1000-digit number that have the greatest product. What is the value of this
# product?

# Answer:
# 23514624000
# ./008.py 13  0.02s user 0.00s system 95% cpu 0.028 total


import sys


def substring_product(i, c, s):
    '''
    Given an integer index, integer count and a string, returns the product of
    the "count" number of elements starting from the index of the string.  The
    string must be entirely composed of integers.  Returns None on out-of-range
    or otherwise invalid inputs.
    '''
    try:
        factors = [int(x) for x in s[i:i+c]]
        if not factors: return None
        return reduce(lambda x, y: x*y, factors) 
    except IndexError:
        return None



def finder(n, filename):
    '''
    Given an integer and a filename containing consecutive integers, returns the
    largest product that can be given by n consecutive integers from the file.
    '''

    # get the source integers from the file
    source = ''
    f = open (filename, 'r')
    for line in f:
        stripped = line.rstrip('\n')
        source += stripped
    
    # initialize loop variables
    largest = 0
    current = 0
    index = 0

    # loop until invalid index is encountered
    while current is not None:
        current = substring_product(index, n, source)
        largest = current if current > largest else largest
        index += 1

    # return largest found product
    return largest


if __name__ == '__main__':
    n = int(sys.argv[1])
    # pprint.pprint(finder(n, 'number'))
    print finder(n, 'number')