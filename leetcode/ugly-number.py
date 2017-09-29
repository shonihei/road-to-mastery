"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example,
6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""

import unittest

def isUgly(num):
    if num == 1:
        return True

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(isUgly(6), True)
