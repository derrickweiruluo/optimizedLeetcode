'''
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.
'''

# Time O(k), k refers to the number of valid permutations
# Space O(n), visited array of size n is used. The depth of recursion tree will also go upto n. Here, n refers to the given integer n.

class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.res = 0
        visited = [0] * (n + 1)  # 1-idx, therefore only 1 to n in interest
        
        def search(n, pos):
            if pos > n: # when search finished
                self.res += 1
            for i in range(1, n + 1):
                if visited[i] == 0 and (pos % i == 0 or i % pos == 0):
                    visited[i] = 1
                    search(n, pos + 1)
                    visited[i] = 0
        
        search(n, 1)
        return self.res