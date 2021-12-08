'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

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

'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if nums[left] == target else -1

        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2 + 1  # 这个是upper bound，所以必须 +1
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            return left if nums[left] == target else -1
        
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return [left, right]