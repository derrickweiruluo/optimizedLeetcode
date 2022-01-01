'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res = math.inf
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == target:
                    return cur
                if abs(target - cur) < abs(target - res):
                    res = cur
                if cur < target:
                    left += 1
                elif cur > target:
                    right -= 1
        
        return res

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res = math.inf
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if abs(target - cur) < abs(target - res):
                    res = cur
                if cur < target:
                    left += 1
                elif cur > target:
                    right -= 1
                else:
                    return cur
        return res