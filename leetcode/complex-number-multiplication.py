"""
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. 
Note i2 = -1 according to the definition.
"""

import unittest

def complexNumberMultiply(a, b):
    a = [int(s) for s in a[:-1].split('+')]
    b = [int(s) for s in b[:-1].split('+')]
    real = 0
    real = (a[0] * b[0]) - (a[1] * b[1])
    imaginary = (a[0] * b[1]) + (a[1] * b[0])
    return "{}+{}i".format(real, imaginary)

class Test(unittest.TestCase):
    def test1(self):
        a = "1+1i"
        b = "1+1i"
        self.assertEqual(complexNumberMultiply(a, b), "0+2i")

    def test2(self):
        a = "1+-1i"
        b = "1+-1i"
        self.assertEqual(complexNumberMultiply(a, b), "0+-2i")

if __name__ == "__main__":
    unittest.main()