"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as
different substrings even they consist of same characters.
"""

def countSubstrings(s):
    count = 0
    for c in range(len(s)):
        odd = centerExpansion(s, c, c)
        even = centerExpansion(s, c, c + 1)
        count += odd + even
    return count

def centerExpansion(s, i, j):
    count = 0
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
        count += 1
    return count

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(countSubstrings("aaa"), 6)


    unittest.main()