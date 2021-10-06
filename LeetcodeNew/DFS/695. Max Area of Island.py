"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(grid, i, j, m, n))
        return res
    
    def dfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        left = self.dfs(grid, i, j - 1, m, n)
        right = self.dfs(grid, i, j + 1, m, n)
        up = self.dfs(grid, i - 1, j, m, n)
        down = self.dfs(grid, i + 1, j, m, n)
        return 1 + left + right + up + down
