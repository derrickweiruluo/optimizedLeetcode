'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        self.dfs(0, n, nums, [], res, k)
        return res
    
    def dfs(self, idx, target, nums, path, res, k):
        if target < 0:
            return
        if target == 0 and len(path) == k:
            res.append(path)
            return
        for i in range(idx, len(nums)):
            self.dfs(i + 1, target - nums[i], nums, path + [nums[i]], res, k)
            
            