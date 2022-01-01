'''
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

 

Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.

'''

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        curSum = 0
        res = 0
        mapping = {0: -1}
        
        for i in range(len(nums)):
            curSum += nums[i]
            # only record the first seen, this will garantee the longest
            # subarray by ensuring the left bound is far left
            if curSum not in mapping: 
                mapping[curSum] = i
            if curSum - k in mapping:
                res = max(res, i - mapping[curSum - k])
        
        return res