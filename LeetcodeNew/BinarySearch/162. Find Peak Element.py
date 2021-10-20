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


解题思路：注意题目条件，1：相邻的元素不会相等。2： 首尾的斜率。

我们可以根据mid本地的斜率来判断指针移动的方向，搜索方向朝向元素增大的一侧。

因为 mid = left+(right-left)/2，所以在 while (left<right) 成立的情况下，mid永远都不会与right重合，因此 nums[mid+1]永远是合法的。 所以我们考察 nums[mid]和nums[mid+1]
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # boundary: all possible values
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        # minimal k that satisfy the 斜率 condition
        return left
