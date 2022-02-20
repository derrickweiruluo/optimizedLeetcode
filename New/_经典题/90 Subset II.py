'''
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
'''


class Solution:  # interview
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        
        def dfs(nums, path, idx):
            res.append(path)
            for i in range(idx, len(nums)):
                if i == idx or nums[i] != nums[i - 1]:
                    # path of [1,2,2,2,2,2,3], only the first 2 is append to the path
                    dfs(nums, path + [nums[i]], i + 1)
        
        dfs(nums, [], 0)
        return res




class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        
        def dfs(nums, path, idx):
            res.append(path)
            for i in range(idx, len(nums)):
                if i == idx or nums[i] != nums[i - 1]:
                    # path of [1,2,2,2,2,2,3], only the first 2 is append to the path
                    dfs(nums[:i] + nums[i + 1:], path + [nums[i]], i)
        
        dfs(nums, [], 0)
        return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        
        def dfs(startIdx, nums, path, res):
            res.append(path)
            for i in range(startIdx, len(nums)):
                if i == startIdx or nums[i] != nums[i - 1]:
                    dfs(i + 1, nums, path + [nums[i]], res)
        
        dfs(0, nums, [], res)
        return res