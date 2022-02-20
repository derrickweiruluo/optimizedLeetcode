'''
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

'''


# Clarifications:
# 每个数字前面 可以添加 '+' or '-'

class Solution:  # BEST, O(sum) space
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        nums_sum = sum(nums)
        if (nums_sum + target) % 2 == 1 or abs(target) > nums_sum:
            return 0
        target_sum = (nums_sum + target) // 2
        dp = [1] + [0] * target_sum
        for num in nums:
            for compliment in range(target_sum, num - 1, -1):
                dp[compliment] += dp[compliment - num]
        return dp[target_sum]

#*-------------------------------------


# Recursion with Memo
# Time: O(sum * n), sum is sum of nums, n is len(nums)
# Space:  O(sum * n), The depth of recursion tree can go up to nn. The memo array contains t \cdot nt⋅n elements

class Solution:
    # https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        memo = {}
        return self.dp(nums, S, index, curr_sum, memo)
        
    def dp(self, nums, target, index, curr_sum, memo):
        # Base Cases
        if (index, curr_sum) in memo:
            return memo[(index, curr_sum)]

        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0 
        
        # Decisions
        positive = self.dp(nums, target, index-1, curr_sum + nums[index], memo)
        negative = self.dp(nums, target, index-1, curr_sum + -nums[index], memo)
        memo[(index, curr_sum)] = positive + negative

        return memo[(index, curr_sum)]


#*-------------------------------------
# LEE

"""
Explanation:
Python solution, but it's really easy to understand.
To make it clear for everyone, find following the syntax for get() method of dictionary(hase map)

It uses a dictionary to store all possible sums using all the numbers 
with +/- signs and return the number of ways of the target sum in the dictionary

"""

# Space: space complexity is the (sum of nums) * 2, when all 1s and all -1s
# time: 2^n, because each state has two states, and n times
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
         
        prev_counter = collections.Counter({0: 1}) # start from 0
        for num in nums:
            cur_counter = collections.Counter()
            for y in prev_counter:
                cur_counter[y + num] += prev_counter[y]
                cur_counter[y - num] += prev_counter[y]
            
            prev_counter = cur_counter
        
        return prev_counter[target]


