"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Ex1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Ex2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Ex3:
Input: nums = [1]
Output: [[1]]
 
Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are UNIQUE.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        # dfs nums缩小和每个index的探索， path + [nums[i]], 每次都从nums pop一个
        def dfs(nums, path):
            if nums == []:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
        
        dfs(nums, [])
        return res
