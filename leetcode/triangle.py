"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
"""

def minimumTotal(triangle):
    if len(triangle) == 0:
        return 0
    if len(triangle[0]) == 0:
        return 0
    i = len(triangle) - 2
    while i >= 0:
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        i -= 1
    return triangle[0][0]

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            t = [
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
            ]
            self.assertEqual(minimumTotal(t), 11)
    
    unittest.main()
