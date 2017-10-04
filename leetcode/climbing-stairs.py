"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
"""

def memoize(f):
    memo = dict()
    def helper(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return helper

def _climbStairs(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return _climbStairs(n - 1) + _climbStairs(n - 2)

def climbStairs(n):
    c = memoize(_climbStairs)
    return c(n)

