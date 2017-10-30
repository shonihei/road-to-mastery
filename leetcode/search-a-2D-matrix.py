"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    left = 0
    right = len(matrix) - 1
    while left < right:
        mid = (left + right) // 2
        if target >= matrix[mid][0] and target <= matrix[mid][-1]:
            break
        else:
            if target > matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid - 1
    else:
        return False

    row = matrix[mid]
    left = 0
    right = len(row) - 1
    while left < right:
        mid = (left + right) // 2
        if target == row[mid]:
            return True
        else:
            if target > row[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return False

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            grid = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
            self.assertTrue(searchMatrix(grid, 3))
    
    unittest.main()
