'''
找一个index切割数组，使左右两边相等, 两边都不包含 nums[idx]
where

'''


# Corner case:
# [-1,-1,-1,0,1,1], should be idx = 0 to cut
# if idx == 0: sum of (null) == sum of (nums[1: ])


# clarifications:
# nums[: idx] == nums[idx + 1: ], nums[idx] does not count

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if leftSum == total - nums[i] - leftSum:
                return i
            leftSum += nums[i]
        
        return -1