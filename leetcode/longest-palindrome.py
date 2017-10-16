"""
Given a string which consists of lowercase or uppercase letters, find the length of the
longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.
"""

def longestPalindrome(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    _max = 0
    max_odd = 0
    odd_c = ""
    for c, f in d.items():
        if f % 2 == 0:
            _max += f
        else:
            if f > max_odd:
                odd_c = c
                max_odd = f
    for c, f in d.items():
        if f % 2 == 1 and c != odd_c:
            _max += f - 1
    return _max + max_odd

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(longestPalindrome("abccccdd"), 7)

    unittest.main()
