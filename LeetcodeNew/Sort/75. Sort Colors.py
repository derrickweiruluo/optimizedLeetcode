"""
75. Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.

#####
n-pointer swapping, sorting implementation
https://www.youtube.com/watch?v=uvB-Ns_TVis
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start,idx, end = 0, 0, len(nums) - 1
        
        while idx <= end and start < end:
            if nums[idx] == 0:
                nums[idx], nums[start] = nums[start], nums[idx]
                idx += 1
                start += 1
            elif nums[idx] == 2:
                nums[idx], nums[end] = nums[end], nums[idx]
                end -= 1
            else:  # if == 1:
                idx += 1
