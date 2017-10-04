"""
[UNFINISHED]
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
"""

def longestPalindrome(s):
    for i in range(len(s)):
        j = i - 1
        k = i + 1
        while 