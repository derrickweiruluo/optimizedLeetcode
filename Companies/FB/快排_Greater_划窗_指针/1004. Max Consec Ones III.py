'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # Find the longest subarray with at most K zeros.

        # 下面的one pass利用了数组只有 0, 1的性质s
        i = 0
        for j in range(len(nums)):
            k -= (1 - nums[j])   # k 代表 quota，每次都会更新
            if k < 0:            # 没 quota 就 i += 1
                k += (1 - nums[i])
                i += 1
        
        return j - i + 1




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