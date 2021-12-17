'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
  

'''
DP:     1, 0, 0, 0, 0,  0, 0
-----------------------------

        1, 1, 1, 1, 1, 1, 1
        1, 2, 3, 4, 5, 6, 7
        1, 3, 6, 10,15,21,28
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [0] * n
        dp[0] = 1
        
        for i in range(0, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        
        return dp[-1]