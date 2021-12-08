'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

'''

class Solution:  # 
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        preSum = collections.Counter()
        preSum[0] = 1  # 这一部很需要，prefix == 0 要 intialize 为 1
        curSum = 0
        
        for num in nums:
            curSum += num
            res += preSum[curSum - k]
            preSum[curSum] += 1
        
        return res



### TLE
class Solution2: # O(n^2), O(1)
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                if cur == k:
                    res += 1
    
        return res