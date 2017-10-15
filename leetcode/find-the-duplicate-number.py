"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
find the duplicate one
"""

def findDuplicate(nums):
    for i in range(len(nums)):
        if nums[abs(nums[i])] < 0:
            return abs(nums[i])
        else:
            nums[abs(nums[i])] = nums[abs(nums[i])] * -1
    return -1

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            self.assertEqual(findDuplicate([1, 1, 2, 3, 4]), 1)

        def test2(self):
            self.assertEqual(findDuplicate([4, 4, 4, 4, 4]), 4)

        def test3(self):
            self.assertEqual(findDuplicate([1,2,2]), 2)

    unittest.main()
