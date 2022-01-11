'''
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
'''

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n - 1):
                matrix[i][j + 1] += matrix[i][j]
        
        res = 0
        for i in range(n):
            for j in range(i, n):
                memo = collections.defaultdict(int)
                cur, memo[0] = 0, 1
                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += memo[cur - target]
                    memo[cur] += 1
        
        return res