"""
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.
"""

def lenghOfLastWord(s):
    s = s.strip()
    out = 0
    i = len(s) - 1
    while i >= 0:
        if s[i] == " ":
            return out
        out += 1
        i -= 1
    return out

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(lenghOfLastWord("a "), 1)

    unittest.main()