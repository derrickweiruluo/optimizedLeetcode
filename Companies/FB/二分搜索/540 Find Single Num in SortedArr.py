'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.


Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Input: nums = [3,3,7,7,10,11,11]
Output: 10
'''


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # Pattern: even, odd, even, odd, ........even, odd
        # left, right as usual, find mid
        
        # if mid is odd, its duplicate is on index - 1,  if satisfy, left = mid + 1
        # if mid is even, its duplicate is on index + 1, if satisfy, left = mid + 1
        
        # if either condition is not satisfied, then the pattern is missed.
        # so, single number must be before mid.
        # so, right -.
        
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1  # 重点，这个题只能 right = len - 1
        
        while left < right:
            mid = (left + right) // 2
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                left = mid + 1
            else:
                right = mid
        
        return nums[left]