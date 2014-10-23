#!/usr/bin/python

# https://projecteuler.net/problem=6

# The sum of the squares of the first ten natural numbers is

# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is

# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

# Answer:
# 25164150
# ./006.py 100  0.02s user 0.00s system 90% cpu 0.017 total


import sys


# The formula for square pyramidal numbers (or a "sum of squares") is a known
# formula that can be derived from the summation notation using induction:
# (n^3 / 3) + (n^2 / 2) + (n / 6)

# The formula for the "square of sums" is simply the square of the known formula
# for a summation (also derived using induction):
# ((n(n+1))/2)^2 which simplifies to
# (n^4 / 4) + (n^3 / 2) + (n^2 / 4)

# When the first is subtracted from the second, the resulting expression is:
# (n^4 / 4) + (n^3 / 6) - (n^2 / 4) - (n / 6)


def main(n):
    return (n**4 / 4) + (n**3 / 6) - (n**2 / 4) - (n / 6)    


if __name__ == '__main__':
    N = int(sys.argv[1])
    print main(N)