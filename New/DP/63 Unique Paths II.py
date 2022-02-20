
'''
2D DP --> 1D DP since the robot can only go down and right
https://leetcode.com/problems/unique-paths-ii/discuss/23250/Short-JAVA-solution

dp[j] += dp[j - 1];
is
dp[j] = dp[j] + dp[j - 1];
which is new dp[j] = old dp[j] + dp[j-1]
which is current cell = top cell + left cell

Hope this helps.
'''

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    # current cell = prev upper cell + left cell
                    dp[j] += dp[j - 1]
        
        return dp[-1]