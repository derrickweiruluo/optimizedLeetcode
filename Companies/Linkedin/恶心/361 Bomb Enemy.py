'''
一个2D grid里面，有士兵，有空格，有墙
问，你只能在空格放炸弹，问你可以最多炸死几个士兵
'''

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        
        
        for i in range(m):
            cur = 0
            for j in range(n):
                if grid[i][j] == 'E':
                    cur += 1
                elif grid[i][j] == 'W':
                    cur = 0
                else:
                    dp[i][j] += cur
        for i in range(m):
            cur = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 'E':
                    cur += 1
                elif grid[i][j] == 'W':
                    cur = 0
                else:
                    dp[i][j] += cur
                    
        for j in range(n):
            cur = 0
            for i in range(m):
                if grid[i][j] == 'E':
                    cur += 1
                elif grid[i][j] == 'W':
                    cur = 0
                else:
                    dp[i][j] += cur
        
        for j in range(n):
            cur = 0
            for i in range(m - 1, -1, -1):
                if grid[i][j] == 'E':
                    cur += 1
                elif grid[i][j] == 'W':
                    cur = 0
                else:
                    dp[i][j] += cur
                    res = max(res, dp[i][j])
        
        return res