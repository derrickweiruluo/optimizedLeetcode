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




# corner cases:
# [1,2,3], res = idx_2
# [3,2,1], res = idx_0



# Clarifications:  #问面试官
# 1.    nums[-1] = nums[n] = -math.inf
# 2.    A peak element is an element that is strictly greater than its neighbors
# 3.    this -math.inf on both ends is the reason why we can use BS, 
#       becasue half of the answer already given
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2

            # 要么右侧方向增大，要么mid本身就是极大点
            if nums[mid] < nums[mid + 1]:
                left = mid + 1   # mid + 1 满足peak左边比他小，搜索右边
            else:       
                right = mid      # mid > mid + 1
        
        
        return left