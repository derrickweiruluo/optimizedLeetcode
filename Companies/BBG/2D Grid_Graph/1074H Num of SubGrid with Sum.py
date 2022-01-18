'''
Given a matrix and a target, return the number of non-empty submatrices that sum to target.
'''

# Explanations: LEE:
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/303750/JavaC%2B%2BPython-Find-the-Subarray-with-Target-Sum

# For each row, calculate the prefix sum.
# For each pair of columns,
# calculate the accumulated sum of rows.
# Now this problem is same to, "Find the Subarray with Target Sum".


# Time O(mnn)
# Space O(m)
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n - 1):
                matrix[i][j + 1] += matrix[i][j]
                
        print(matrix)
        
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