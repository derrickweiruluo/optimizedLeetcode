'''
给一个 nums = [1 to n] 的数组，找出beautiful arrangement的数量

Beautiful:: 
     1. nums[i] % i == 0
  OR 2. i % nums[i] == 0  

'''

class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.cache = {}
        def helper(i, X):
            if i == 1:
                return 1
            key = (i, X)
            if key in self.cache:
                return self.cache[key]
            
            total = 0
            for j in range(len(X)):
                if X[j] % i == 0 or i % X[j] == 0:
                    total += helper(i - 1, X[:j] + X[j + 1:])
            self.cache[key] = total
            return total
        return helper(n, tuple(range(1, n + 1)))



class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.res = 0
        visited = [0] + [0] * n
        
        def search(n, pos):
            if pos > n:
                self.res += 1
            for i in range(1, n + 1):
                if visited[i] == 0 and (pos % i == 0 or i % pos == 0):
                    visited[i] = 1
                    search(n, pos + 1)
                    visited[i] = 0
        
        search(n ,1)
        return self.res