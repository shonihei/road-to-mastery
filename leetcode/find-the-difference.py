"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one 
more letter at a random position.

Find the letter that was added in t.
"""

import unittest

def findDifference(s, t):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    for c in t:
        if c not in d or d[c] == 0:
            return c
        else:
            d[c] -= 1
    return None

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(findDifference("abcd", "abcde"), "e")
    
    def test2(self):
        self.assertEqual(findDifference("bcde", "badce"), "a")

if __name__ == "__main__":
    unittest.main()