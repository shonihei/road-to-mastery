"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
"""

import unittest

def getSum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return getSum((a ^ b), ((a & b) << 1))

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(getSum(3, 4), 7)

    def test2(self):
        self.assertEqual(getSum(-5, 4), -1)
    
    def test3(self):
        self.assertEqual(getSum(0, 0), 0)

    def test4(self):
        self.assertEqual(getSum(2, 3), 5)
    
    def test5(self):
        self.assertEqual(getSum(100002, 45232), 145234)

    def test6(self):
        self.assertEqual(getSum(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()
