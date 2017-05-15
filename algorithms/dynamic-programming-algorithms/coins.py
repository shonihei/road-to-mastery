# task: given a list of N coins, their values, and the total mass S, Find the minimum number of coins the sum of which is S.

def minimum_coins(coins, S):
    if not coins:
        return 0
    
