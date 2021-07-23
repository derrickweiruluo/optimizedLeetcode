class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def dfs(nums, path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                if i + 1 < len(nums) and nums[i] != nums[i + 1] or i == len(nums) - 1:
                    dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
        
        
        dfs(sorted(nums), [])
        return res
    
#   1 <= nums.length <= 8
#   -10 <= nums[i] <= 10
