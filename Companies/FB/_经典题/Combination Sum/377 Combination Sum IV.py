'''这个问题其实是permuatation

Input: nums = [1,2,3], target = 4
Output: 7

Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
'''

# 这个问题其实是permuatation
# space; O(target), time: O(target * n) ~ O(n)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [1] + [0] * target
        # nums.sort()
        
        # either sort first and break during the inner loop
        # or not sort, but continue looping the entire array
        for i in range(1, target + 1):
            dp[i] = sum(dp[i - num] for num in nums if i >= num)
    
        return dp[-1]
        
# dp start:[1, 0, 0, 0, 0, 0, 0, 0]
#          [1, 1, 0, 0, 0, 0, 0, 0]
#          [1, 1, 2, 0, 0, 0, 0, 0]
#          [1, 1, 2, 4, 0, 0, 0, 0]
#          [1, 1, 2, 4, 7, 0, 0, 0]
#          [1, 1, 2, 4, 7, 13, 0, 0]
#          [1, 1, 2, 4, 7, 13, 24, 0]
#          [1, 1, 2, 4, 7, 13, 24, 44]



# * -----------------------------
# # FOLLOW UP: 
# What if negative numbers are allowed in the given array? How does it change the problem? 
# What limitation we need to add to the question to allow negative numbers?
class Solution(object):
    def combinationSum4(self, nums, target, length, memo=collections.defaultdict(int)):
        if length <= 0: return 0
        if length == 1: return 1 * (target in nums)
        if (target, length) not in memo: 
            for num in nums:
                memo[target, length] += self.combinationSum4(nums, target - num, length - 1)
        return memo[target, length]