"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
"""

import unittest

def rotate(nums, k):
    for _ in range(k):
        nums.insert(0, nums.pop())

class Test(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        rotate(nums, k)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()    
