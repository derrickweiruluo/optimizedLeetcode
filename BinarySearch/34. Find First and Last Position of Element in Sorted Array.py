"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

  Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

  Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

#####
def一个通用二分函数， 找target的左位置， 找target + 1 的前一位
确认边界和确认target存在
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums: return [-1, -1]
        
        n = len(nums)
        if n == 1: return [0, 0] if nums[0] == target else [-1, -1]
        
        def search(target):
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        lo = search(target)
        if lo >= n or nums[lo] != target:
            return [-1, -1]
        
        hi = search(target + 1) - 1
        return [lo, hi]
