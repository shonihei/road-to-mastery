"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination
of the coins, return -1.
"""

def coinChange(coins, amount):
    memo = {}
    def f(coins, amount):
        if amount in memo:
            return memo[amount]
        else:
            if amount == 0:
                memo[amount] = 0
            elif amount < min(coins):
                memo[amount] = 0x7fffffff
            else:
                _min = 0x7fffffff
                for coin in coins:
                    _min = min(_min, f(coins, amount - coin) + 1)
                memo[amount] = _min
            return memo[amount]
    out = f(coins, amount)
    return -1 if out == 0x7fffffff else out