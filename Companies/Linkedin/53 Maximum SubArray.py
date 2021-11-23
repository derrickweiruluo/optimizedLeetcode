

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curMax = -math.inf
        res = nums[0]
        
        for i in range(len(nums)):
            curMax = max(curMax + nums[i], nums[i])
            res = max(res, curMax)
        
        return res