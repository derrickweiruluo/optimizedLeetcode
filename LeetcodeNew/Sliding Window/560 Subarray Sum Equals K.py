'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSum = collections.defaultdict(int)
        prefixSum[0] = 1
        
        for i, num in enumerate(nums):
            curSum += num
            res += prefixSum[curSum - k]
            prefixSum[curSum] += 1
        
        return res