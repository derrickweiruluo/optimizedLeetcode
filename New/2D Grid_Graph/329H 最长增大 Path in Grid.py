# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# 4-directions only
# 求最长的 increasing 路径是有多长

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix: return 0
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(matrix)
        n = len(matrix[0])
        cache = [[-1 for _ in range(n)] for _ in range(m)]  # memorization to eliminate duplicate searching
        res = 1
        
        for i in range(m):
            for j in range(n):
                cur_len = self.dfs(i, j, matrix, cache, m, n)
                res = max(res, cur_len)
        return res
    
    def dfs(self, i, j, matrix, cache, m, n):
        if cache[i][j] != -1:
            return cache[i][j]
        res = 1
        for direction in self.directions:
            x, y = i + direction[0], j + direction[1]
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                cur_length = 1 + self.dfs(x, y, matrix, cache, m, n)   # for this (i, j), 1 + dfs_length
                res = max(res, cur_length)         # during dfs, res could be updated and compare w/ new val
        cache[i][j] = res
        return res