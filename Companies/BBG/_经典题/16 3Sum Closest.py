'''
Input: nums = [-1,2,1,-4], target = 1
Output: 2
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