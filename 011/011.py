#!/usr/bin/python

# https://projecteuler.net/problem=11
# In the 20x20 grid below, four numbers along a diagonal line have been marked
# in red.  The product of these numbers is 26 * 63 * 78 * 14 = 1788696.  What is
# the greatest product of four adjacent numbers in the same direction (up, down,
# left, right, or diagonally) in the 20x20 grid?

# Answer:
# 70600674
# ./011.py 4  0.02s user 0.01s system 88% cpu 0.030 total


import sys


def read_file(filename):
    '''
    Given a filename, returns a 2D list with its contents.
    '''
    f = file(filename, 'r')
    result = []
    for raw_line in f:
        line = [int(x) for x in raw_line.split(' ')]
        result.append(line)
    return result


def get_value(x, y, direction, number, grid):

    if direction == 'w':
        a = 1
        b = 0
    elif direction == 'sw':
        a = 1
        b = 1
    elif direction == 's':
        a = 0
        b = 1
    elif direction == 'se':
        a = -1
        b = 1

    try:
        values = list()
        for i in range(number):
            j = x + (i*a)
            k = y + (i*b)
            if j < 0: raise IndexError
            if k < 0: raise IndexError
            values.append(grid[j][k])

        return (reduce(lambda x, y: x*y, values))

    except IndexError:
        return None


def find(number):

    grid = read_file('numbers')
    directions = ['w', 'sw', 's', 'se']
    maxvalue = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for direction in directions:
                value = get_value(i, j, direction, number, grid)
                maxvalue = max(value, maxvalue)

    return maxvalue


if __name__ == '__main__':
    n = int(sys.argv[1])
    print find(n)