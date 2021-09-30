# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
////


class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        # Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time 
        # results in the array          [a[n-1], a[0], a[1], a[2], ..., a[n-2]]
        # # rotate指的是当前最后的一个放最前面
        # which means, when ever we find nums[mid] < nums[right], 答案就在 (left, right]
        
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
