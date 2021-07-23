class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        nums.sort()
        
        max_diff = 0
        for i in range(1, n):
            max_diff = max(max_diff, abs(nums[i] - nums[i - 1]))
        return max_diff
      
# 一次过，easy
