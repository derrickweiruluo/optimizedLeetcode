"""

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

dp[i][j] means the size of biggest square with A[i][j] as bottom-right corner.
dp[i][j] also means the number of squares with A[i][j] as bottom-right corner.

If A[i][j] == 0, no possible square.
If A[i][j] == 1,
we compare the size of square dp[i-1][j-1], dp[i-1][j] and dp[i][j-1].
min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 is the maximum size of square that we can find.

Complexity
Time O(MN)
Space O(1)
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # case of size > 1, see note above
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                
                res += matrix[i][j]  # base case for adding size-1 square
                    
        return res
                
