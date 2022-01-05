'''
Combination sum with conditions of:

1. input contain duplicates
2. output, each sub-result can only use the input num ONCE
'''

# Time complexity is O(2^n). Space complexity O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        self.dfs(target, candidates, [], res)
        return res
    
    def dfs(self, target, nums, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(0, len(nums)):
            if i == 0 or nums[i] != nums[i - 1]: # 除重， 下一步dfs必须是 i + 1
                self.dfs(target - nums[i], nums[i + 1:], path + [nums[i]], res)



# Time complexity is O(2^n). Space complexity O(n)
class Solution: # same solution as above
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        
        def dfs(nums, path, target, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    dfs(nums[i + 1:], path + [nums[i]], target - nums[i], res)
        
        dfs(candidates, [], target, res)
        return res