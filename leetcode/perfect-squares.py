"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""

def numSquares(n):
    dp = [0, 1, 2, 3]
    if n < len(dp):
        return dp[n]
    i = 4
    while i <= n:
        j = 1
        _min = float('inf')
        while j*j <= i:
            _min = min(_min, dp[i - j*j] + 1)
            j += 1
        dp.append(_min)
        i += 1
    return dp[n]
