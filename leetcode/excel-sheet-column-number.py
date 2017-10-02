"""
Given a column title as appear in an Excel sheet,
return its corresponding column number.
"""

import unittest

def titleToNumber(s):
    total = 0
    mult = 1
    i = len(s) - 1
    while i >= 0:
        c = s[i]
        num = ord(c) - 64
        total += num * mult
        mult *= 26
        i -= 1
    return total

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(titleToNumber("AA"), 27)
    
    def test2(self):
        self.assertEqual(titleToNumber("A"), 1)

if __name__ == "__main__":
    unittest.main()