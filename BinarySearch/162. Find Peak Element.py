"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.



#############
We need to find place k, such that nums[k] < nums[k+1] and nums[k+1] > nums[k+2]. Let us compare all pairs of adjacent elements and ask question: if the first one is smaller then the second, for our array we have [True, True, False, True, True, True, False, False]. Then what we need to find in this array is any two adjacent places where we have pair True, False. Note, that first element is always True and last is always False, so we have True, .............., False.

"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return left
