"""
Given an array containing n distinct numbers taken from
0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.
"""

def missingNumber(nums):
    total = 0
    for i in range(len(nums) + 1):
        total += i
    
    for n in nums:
        total -= n
    return total

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(missingNumber([0, 1, 3]), 2)
        
        def test2(self):
            self.assertEqual(missingNumber([4, 3, 6, 2, 0, 1]), 5)
    
    unittest.main()