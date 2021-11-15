'''
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:

Input: n = 37
Output: []
Example 4:

Input: n = 32
Output: [[2,16],[4,8],[2,2,8],[2,4,4],[2,2,2,4],[2,2,2,2,2]]
'''

class Solution:  # 下面是comment 一样的solution
    def getFactors(self, n: int) -> List[List[int]]:
        
        res = []
        def dfs(x, start, path):
            if path:
                res.append(path + [x])
            for i in range(start, int(x ** 0.5) + 1):
                if x % i == 0:
                    dfs(x // i, i, path + [i])

        dfs(n, 2, [])
        return res
    
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        # https://leetcode.com/problems/factor-combinations/discuss/943983/Python-Recursive-DFS-or-Beats-95-or-Explanation-or-Easy
        
        def dfs(x, start, path):
            # start is the start divisor, we want to eliminate duplicate, 
            # so from small to big, we divide them repeating before advance to the next
            if path:
                res.append(path + [x])
            
            # use sqrt because 3 * 6 and 6 * 3 is the same, eliminate duplicate combo like that
            for i in range(start, int(x ** 0.5) + 1):  
                if x % i == 0:
                    dfs(x // i, i, path + [i])
        
        res = []
        dfs(n, 2, [])
        return res