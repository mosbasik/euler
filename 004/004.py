#!/usr/bin/python

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


import sys


def isPalindrome(N):
    strN = str(N)
    return True if strN == strN[::-1] else False


def greatestNDigitProductPalindrome(N):
    result = []
    for i in range(10**(N-1), (10**N)-1):
        for j in range(10**(N-1), (10**N)-1):
            if isPalindrome(i*j):
                result.append(i*j)
    return max(result)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print greatestNDigitProductPalindrome(n)