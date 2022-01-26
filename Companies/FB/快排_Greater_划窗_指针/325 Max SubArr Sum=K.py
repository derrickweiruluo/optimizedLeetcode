class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        curSum = 0
        res = 0
        mapping = {0: -1}
        
        for i in range(len(nums)):
            curSum += nums[i]
            # only record the first seen, this will garantee the longest
            # subarray by ensuring the left bound is far left

            # 前锤和只取第一次看到的indx，这样保证window最大
            if curSum not in mapping: 
                mapping[curSum] = i
            if curSum - k in mapping:
                res = max(res, i - mapping[curSum - k])
        
        return res