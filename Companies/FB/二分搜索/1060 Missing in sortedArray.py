'''
nums is Sorted in ASCENDING Order

Find the xth missing number
'''

# Clarifications:
# Sorted and Increasing

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        if not nums or k == 0: 
            return 0
        
        completeLength = nums[-1] - nums[0] + 1. # complete length from [start_num: end_num]
        missing = completeLength - len(nums)
        if missing < k:
            return int(nums[-1] + (k - missing))
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            missing = nums[mid] - nums[0] - (mid - 0)
            print(missing)
            if missing < k:
                left = mid + 1
            else:
                right = mid
        print(left)
        return nums[0] + k + left - 1   # at pos left, it is th result that has more than k spot, therefore, left - 1 at the end