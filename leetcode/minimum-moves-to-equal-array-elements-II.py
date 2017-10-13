"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal,
where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.
"""

def minMoves2(nums):
    nums.sort()
    median_i = len(nums) // 2
    median = nums[median_i]
    moves = 0
    for i in range(len(nums)):
        moves += abs(nums[i] - median)
    return moves

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(minMoves2([1, 2, 3]), 2)

    unittest.main()
