'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        zero_count = 0
        i = 0
        res = 0
        
        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1
            res = max(res, j - i + 1)
        
        return res