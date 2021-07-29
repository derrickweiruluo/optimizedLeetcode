class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # sliding window option
        
        startIdx = 0
        res = len(nums) + 1
        
        for i in range(len(nums)):
            target -= nums[i]
            while target <= 0:  # SUM from startIdx to current index >= target
                res = min(res, i - startIdx + 1)
                target += nums[startIdx]
                startIdx += 1
        
        return res if res < len(nums) + 1 else 0
