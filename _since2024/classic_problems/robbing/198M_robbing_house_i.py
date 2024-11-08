"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. creating traditional DP
        # dp = [0] * (len(nums) + 2)
        # for i, num in enumerate(nums):
        #     dp[i] += num

        # 2. quicker way of creating dp array
        dp = nums + [0] * 2
        prev_2, prev_1 = 0, 0
        for val in dp:
            prev_2, prev_1 = prev_1, max(prev_2 + val, prev_1)
        return prev_1
