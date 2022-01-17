'''
Input: nums = [-2,0,1,3], target = 2
Output: 2

Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
'''

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res = 0
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur < target:
                    res += (right - left)
                    left += 1
                else:
                    right -=1
        
        return res