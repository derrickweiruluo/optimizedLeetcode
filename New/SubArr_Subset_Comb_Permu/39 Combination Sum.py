'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target
'''

# Clarifications:

# 1. You may return the combinations in any order.
# 2. The same number may be chosen from candidates an unlimited number of times. 
# all elem in input is unique



#  k is average length of each solution, and we need O(k)
# time: O(k * 2 ^ n), for solution is 2^n
# Space # O(n) for path and recursion. O(2n)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # https://leetcode.com/submissions/detail/586325101/
        
        res = []
        
        def dfs(nums, path, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i:], path + [nums[i]], target - nums[i])
        
        dfs(candidates, [], target)
        return res



# Leetcode 40