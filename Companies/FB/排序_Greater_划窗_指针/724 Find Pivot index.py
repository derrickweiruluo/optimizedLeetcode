# 找到一个pivot
# nums = nums = [1,7,3,6,5,6]
# left = [1,7,3] = 11
# pivot = [6] @ index 3
# right = [5,6] = 1

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        numsSum = sum(nums)
        leftSum = 0
        
        # pivot is not in the sum of left or right
        
        for i, val in enumerate(nums):
            if leftSum == (numsSum - leftSum - val):
                return i
            leftSum += val
        
        return -1
        