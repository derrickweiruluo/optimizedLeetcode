'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.



'''

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        if not grid:
            return 0
        
        def dfs(i, j, val):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = val
                dfs(i + 1, j, val)
                dfs(i - 1, j, val)
                dfs(i, j + 1, val)
                dfs(i, j - 1, val)
        
        # 先把四个边，以及dfs可达到的，从 water 变成 island
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and grid[i][j] == 0:
                    dfs(i, j, 1)
                    
        # and then the problem becomes count island
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 1)
                    res += 1
        
        return res
