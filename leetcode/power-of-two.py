"""
Given an integer, write a function to determine if it is a power of two.
"""

from math import log
def isPowerOfTwo(self, n):
    if n <= 0:
        return False
    return (2 ** int(log(n, 2))) == n