"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array
elements equal, where a move is incrementing n - 1 elements by 1.
"""

def minMoves(nums):
    _max = max(nums)
    count = 0
    for n in nums:
        count += _max - n
    return count