"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""

def searchInsert(nums, target):
    i = 0
    while i < len(nums) and target > nums[i]:
        i += 1
    return i

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(searchInsert([1, 2, 5, 7], 3), 2)
        
        def test2(self):
            self.assertEqual(searchInsert([1], 0), 0)
    
    unittest.main()
