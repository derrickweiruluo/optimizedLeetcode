'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        prefix = collections.defaultdict(int)
        prefix[0] = 1  # 这一部很需要，prefix == 0 要 intialize为1
        cur = 0
        
        for i in range(len(nums)):
            cur += nums[i]
            res += prefix[cur - k]
            prefix[cur] += 1
        
        return res