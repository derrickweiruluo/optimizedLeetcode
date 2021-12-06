class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m, n = len(points), len(points[0])
        dp = points
        
        for i in range(m - 1):
            for j in range(1, n):
                dp[i][j] = max(dp[i][j], dp[i][j - 1] - 1)
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(dp[i][j], dp[i][j + 1] - 1 if j != n - 1 else 0)
                dp[i + 1][j] += dp[i][j]
        
        return max(dp[-1])
                