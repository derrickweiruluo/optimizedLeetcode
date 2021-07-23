class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(nums, path):
            if nums == []:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
        
        dfs(nums, [])
        
        return res

#    1 <= nums.length <= 6
#    -10 <= nums[i] <= 10
#    All the integers of nums are unique.
