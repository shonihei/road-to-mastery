"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
"""

def longestPalindromeSubseq(s):
    return _longestPalindromeSubseq(s, 0, len(s) - 1)

memo = {}
def _longestPalindromeSubseq(s, i, j):
    if (s, i, j) in memo:
        return memo[(s, i, j)]
    else:
        if i > j:
            memo[(s, i, j)] = 0
        elif i == j:
            memo[(s, i, j)] = 1
        elif s[i] == s[j]:
            memo[(s, i, j)] = 2 + _longestPalindromeSubseq(s, i + 1, j - 1)
        else:
            memo[(s, i, j)] = max(_longestPalindromeSubseq(s, i + 1, j), _longestPalindromeSubseq(s, i, j - 1))
        return memo[(s, i, j)]