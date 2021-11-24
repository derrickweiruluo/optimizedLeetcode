'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def dfs(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
        
        # k = [1]
        # print(k[50:51], k[100:], k[:0] + k[1:])
        
        dfs(nums, [])
        return res