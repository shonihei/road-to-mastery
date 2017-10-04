"""
[UNFINISHED]

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

def canJump(nums):
    i = 0
    while True:
        if i == len(nums) - 1:
            return True
        jump = nums[i]
        if jump == 0:
            return False
        if i + jump > len(nums) - 1:
            return False
        i += jump

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertTrue(canJump([2, 3, 1, 1, 4]))
        
        def test2(self):
            self.assertFalse(canJump([2, 3, 0, 0, 0]))
        
        def test3(self):
            self.assertTrue(canJump([0]))

    unittest.main()
