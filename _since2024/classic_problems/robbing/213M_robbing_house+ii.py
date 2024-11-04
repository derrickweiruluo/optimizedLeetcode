"""
Same condition as House robbing i, but houses are circular now
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        def rob_liner(arr):
            dp = arr + [0] * 2  
            prev_2, prev_1 = 0, 0
            for val in dp:
                prev_2, prev_1 = prev_1, max(prev_2 + val, prev_1)
            return prev_1

        arr1 = nums[1:]
        arr2 = nums[: len(nums) - 1]
        arr3 = nums[1 : len(nums) - 1]
        return max(rob_liner(arr1), rob_liner(arr2), rob_liner(arr3))
