"""
Given an arbitrary ransom note string and another string containing letters
from all the magazines, write a function that will return true if the ransom
note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
"""

import unittest

def canConstruct(ransomNote, magazine):
    d = dict()
    for c in magazine:
        d[c] = d.get(c, 0) + 1
    
    for c in ransomNote:
        if c in d and d[c] > 0:
            d[c] -= 1
        else:
            return False
    return True

class Test(unittest.TestCase):
    def test1(self):
        self.assertFalse(canConstruct("a", "b"))
    
    def test2(self):
        self.assertTrue(canConstruct("aa", "aab"))
    
    def test3(self):
        self.assertFalse(canConstruct("aa", "ab"))
    
if __name__ == "__main__":
    unittest.main()
