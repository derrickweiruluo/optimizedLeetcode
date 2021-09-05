"""
Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
 

Constraints:

1 <= firstLen, secondLen <= 1000
2 <= firstLen + secondLen <= 1000
firstLen + secondLen <= nums.length <= 1000
0 <= nums[i] <= 1000
"""

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        if len(nums) == firstLen + secondLen:
            return sum(nums)
        
        res = 0
        n = len(nums)
        
        for i in range(firstLen - 1, n - secondLen):
            res = max(res, self.maxSub(nums[:i + 1], firstLen) + self.maxSub(nums[i + 1:], secondLen))
            print(res, 1, i)
        
        for i in range(secondLen - 1, n - firstLen):
            res = max(res, self.maxSub(nums[:i + 1], secondLen) + self.maxSub(nums[i + 1:], firstLen))
            print(res, 2, i)
        
        
        return res
    
    
    def maxSub(self, nums, l):
        res = 0
        for i in range(0, len(nums) - l + 1):
            res = max(res, sum(nums[i: i + l]))
        
        return res
    
    
"""
[4,5,14,16,16,20,7,13,8,15]
3
5
"""
