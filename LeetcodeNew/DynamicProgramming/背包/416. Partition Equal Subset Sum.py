"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
subsum_set and check every num for target

Example 1:
Input: nums = [1,5,11,5]  --> [1, 5, 5] and [11]
Output: true

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

'''
DP解法 01背包问题, 一维空间 from 0 to target
残酷刷题群群主的模板
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        # if weight not divisible by two, we cannot possibly have two equal sets
        if numSum % 2 != 0:
            return False
        
        # target is weight of the knapsack
        target = numSum // 2
        
        # dp init
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        
        for i in range(len(nums)): # 遍历背包物品
            for j in range(target + 1): # 遍历容量
                if dp[j - i]:
                    dp[j] = True
        
        return dp[target]


class SolutionDP:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        # if weight not divisible by two, we cannot possibly have two equal sets
        if numSum % 2 != 0:
            return False
        
        # target is weight of the knapsack
        target = numSum // 2
        
        # dp init
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        
        # j is weight bound, and i is arr pointer.
        # dp[j] :: for a weight j, can we partition into two equal sets with elements 0..i
        for i in range(len(nums)):
            # reversal neessary, because if we go in non-reversed order, we will overwrite
            # dp[] calculations from the previous iteration of outer loop. thus we go small to big to preserve previous iteration
            for j in reversed(range(1, target + 1)):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]
        
        return dp[target]

class SolutionDFS:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        if sum(nums) % 2 == 1: 
            return False
        target = sum(nums) // 2     #target sum 
        subsums_set = set([0])      #stores the sums of the subsets
        
        for num in nums:
            sum_with_num = []       #stores the sums of the subsets that contain "num"
            for sub_sum in subsums_set:
                if num + sub_sum == target:
                    return True
                if num + sub_sum < target:
                    sum_with_num.append(num + sub_sum)
            
            subsums_set.update(sum_with_num)
        
        return False
