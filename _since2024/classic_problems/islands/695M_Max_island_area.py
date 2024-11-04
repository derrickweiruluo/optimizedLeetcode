"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def dfs(grid, i, j):
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != 1:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = -1
            left = dfs(grid, i, j - 1)
            right = dfs(grid, i, j + 1)
            up = dfs(grid, i - 1, j)
            down = dfs(grid, i + 1, j)
            return 1 + left + right + up + down

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(grid, i, j))

        return res
