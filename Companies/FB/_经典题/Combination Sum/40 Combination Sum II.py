'''
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''

# Duplicate not allowed

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        
        def dfs(nums, path, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    dfs(nums[i + 1:], path + [nums[i]], target - nums[i])
        
        
        dfs(candidates, [], target)
        return res