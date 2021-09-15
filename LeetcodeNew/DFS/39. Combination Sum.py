"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


#######
DFS构建每一个子解
input array是unique的，且允许多次使用同一个nums[i]
input array里都是正数
"""



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(target, candidates, [], res)
        return res
    
    def dfs(self, target, nums, path, res):
        if target < 0: # all positive number, if subtract to 0, it is a dead end
            return
        if target == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            # need to search from nums[i:] because each num can use multiple times
            self.dfs(target - nums[i], nums[i:], path + [nums[i]], res)
