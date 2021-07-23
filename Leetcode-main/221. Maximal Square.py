class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        max_side = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
                    max_side = max(max_side, dp[i + 1][j + 1])
        
        
        return max_side ** 2
