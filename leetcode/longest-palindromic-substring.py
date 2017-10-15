"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""

def longestPalindrome(s):
    max_length = 0
    for c in range(len(s)):
        i = c - 1
        j = c + 1
        length = 1
        while i >= 0 and s[i] == s[c]:
            i -= 1
        while j < len(s) and s[j] == s[c]:
            j += 1
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        if j - i - 1 > max_length:
            max_length = j - i - 1
            longest_substring = s[i+1:i+1+max_length]
    return longest_substring

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(longestPalindrome("bbabb"), "bbabb")

        def test2(self):
            self.assertEqual(longestPalindrome("cbbd"), "bb")

    unittest.main()
