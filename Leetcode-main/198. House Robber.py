class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * 101
        for i, num in enumerate(nums):
            dp[i] += num
        
        
        prev, curr = 0, 0
        for i in range(len(dp)):
            prev, curr = curr, max(prev + dp[i], curr)
            
        return curr
            
