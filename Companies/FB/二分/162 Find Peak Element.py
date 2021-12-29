'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
'''


# Clarifications and corner cases:
'''
for len of n, 0 to n - 1
nums[-1] = nums[n] = -math.inf
this -math.inf is the reason why we can use BS, becasue half of the answer already given

corner cases:
[1,2,3], res = idx_2
[3,2,1], res = idx_0
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[mid + 1]:  # 假如右peak满足
                right = mid                 # 搜索右边，包含mid
            else:                           # 假如不满足
                left = mid + 1              # 搜索左边，不包含mid，因为不符合条件
        
        
        return left