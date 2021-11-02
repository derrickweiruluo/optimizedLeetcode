'''
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

'''

class Solution:
    def countArrangement(self, n: int) -> int:
        self.res = 0
        
        def dfs(n, pos, visited):
            if pos > n: self.res += 1
            for i in range(1, n + 1):
                if visited[i] == 0 and (pos % i == 0 or i % pos == 0):
                    visited[i] = 1
                    dfs(n, pos + 1, visited)
                    visited[i] = 0
        
        visited = [0] * (n + 1)
        dfs(n, 1, visited)
        return self.res