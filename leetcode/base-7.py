"""
Given an integer, return its base 7 string representation.
"""

def convertToBase7(num):
    if num == 0:
        return "0"
    neg = False
    if num < 0:
        neg = True
        num *= -1
    out = ""
    while num > 0:
        out = str(num % 7) + out
        num //= 7
    return out if not neg else "-" + out 

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(convertToBase7(100), "202")
        
        def test2(self):
            self.assertEqual(convertToBase7(-7), "-10")

    unittest.main()