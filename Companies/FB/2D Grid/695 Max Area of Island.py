'''
如题
求最大岛屿的面积
岛屿包含空心岛
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, self.dfs(grid, i, j, m, n))
        return res
    
    def dfs(self, grid, i, j, m, n):
        if i < 0 or i > m - 1 or j < 0 or j > n - 1 or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        left = self.dfs(grid, i - 1, j, m, n)
        right = self.dfs(grid, i + 1, j, m, n)
        up = self.dfs(grid, i, j - 1, m, n)
        down = self.dfs(grid, i, j + 1, m, n)
        return 1 + left + right + up + down