class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        # This is a patter of even, odd, even, odd, ........even, odd
        # left, right as usual, find mid
        
        # if mid is odd, its duplicate is on index - 1,  if satisfy, left = mid + 1
        # if mid is even, its duplicate is on index + 1, if satisfy, left = mid + 1
        
        # if either condition is not satisfied, then the pattern is missed.
        # so, single number must be before mid.
        # so, right -.
        
        left, right = 0, len(nums) - 1  # 重点，这个题只能 right = len - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
