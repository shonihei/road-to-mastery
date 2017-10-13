"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.
"""

def numIslands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                if i - 1 >= 0 and grid[i - 1][j] == "1":
                    continue
                if j - 1 >= 0 and grid[i][j - 1] == "1":
                    continue
                count += 1
    return count

if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        def test1(self):
            grid = [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ]
            self.assertEqual(numIslands(grid), 1)

    unittest.main()
