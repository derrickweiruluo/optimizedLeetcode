'''
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n
        left = right = 1 # to make both preSum pointers lag by one digit
        for i in range(n):
            j = -1 - i
            res[i] *= left
            res[j] *= right
            left *= nums[i]
            right *= nums[j]
        
        return res