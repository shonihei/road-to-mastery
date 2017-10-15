"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

def uniquePaths(m, n):
    grid = [[0 for i in range(n)] for j in range(m)]
    for j in range(n):
        grid[0][j] = 1
    for i in range(m):
        grid[i][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[-1][-1]

