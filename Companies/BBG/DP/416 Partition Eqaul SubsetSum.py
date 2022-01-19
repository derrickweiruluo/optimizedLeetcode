'''
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
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
        
        # j is weight bound, and i is arr pointer.
        # dp[j] :: for a weight j, can we partition into two equal sets with elements 0..i
        for i in range(len(nums)):
            # reversal neessary, because if we go in non-reversed order, we will overwrite
            # dp[] calculations from the previous iteration of outer loop. thus we go small to big to preserve previous iteration
            for j in range(target, 0, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]
            
            # print(dp)
        
        return dp[target]
    


# DFS MEMO
# Let N be the number of array elements and M be the subSetSum.
# Time O(N * M) and Space O(N * M)

# In the worst case where there is no overlapping calculation, the maximum number of entries in the memo would be M * N. For each entry, overall we could consider that it takes constant time, i.e. each invocation of dfs() at most emits one entry in the memo.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:        
        def dfs(nums, target, cache):
            if target < 0: return False
            if target == 0: return True
            if target in cache: return False
            cache.add(target)
            for i, n in enumerate(nums):
                if dfs(nums[i+1:], target-n, cache): return True
            return False

        target = sum(nums)
        if target % 2 != 0: return False
        return dfs(nums, target//2, set())