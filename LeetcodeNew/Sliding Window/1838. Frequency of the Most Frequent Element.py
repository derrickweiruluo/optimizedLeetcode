'''
The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

Examples:

Input: nums = [1,2,4], k = 5
Output: 3
[4,4,4]


Input: nums = [1,4,8,13], k = 5
Output: 2
[4,4,8,13], [1,8,8,13], [1,4,13,13]

Input: nums = [3,9,6], k = 2
Output: 1
'''

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        i = 0       # left of the sliding window
        res = 0     # length of the sliding window which is the res
        nums.sort() # sort is needed
        
        for j in range(len(nums)):
            k += nums[j]            # growing wondow to the right
            if k < nums[j] * (j - i + 1):   # condition is perSum < windowLen * curNum
                k -= nums[i]                # shrink the left window and advance left 
                i += 1
            res = max(res, j - i + 1)
        
        return res
