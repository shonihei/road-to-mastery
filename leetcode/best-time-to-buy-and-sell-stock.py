"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), design an algorithm to find
the maximum profit.
"""

def maxProfit(prices):
    if len(prices) < 2:
        return 0
    max_profit = 0
    cur_min = prices[0]
    for price in prices[1:]:
        if price - cur_min > max_profit:
            max_profit = price - cur_min
        if price < cur_min:
            cur_min = price
    return max_profit


