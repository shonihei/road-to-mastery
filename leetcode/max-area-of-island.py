"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
"""

def maxAreaOfIsland(grid):
    visited = [[False for i in range(len(row))] for row in grid]
    max_size = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not visited[i][j]:
                size = traverse(grid, i, j, visited)
                if size > max_size:
                    max_size = size
    return max_size

def traverse(grid, i, j, visited):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 0
    if grid[i][j] == 0 or visited[i][j]:
        return 0
    else:
        visited[i][j] = True
        return 1 + traverse(grid, i - 1, j, visited) + traverse(grid, i, j - 1, visited) + traverse(grid, i, j + 1, visited) + traverse(grid, i + 1, j, visited)
        
            
