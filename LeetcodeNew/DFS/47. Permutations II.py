"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10


#######
if i == 0 or nums[i] != nums[i - 1]查重
 
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(nums, path):
            if nums == []:
                res.append(path)
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
        
        
        dfs(sorted(nums), [])
        return res
