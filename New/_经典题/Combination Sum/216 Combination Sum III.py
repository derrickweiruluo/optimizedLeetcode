'''
I   题目要求 可以重复
II  题目要求 不能重复
III 题目要求 不能重复使用且有长度限制

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