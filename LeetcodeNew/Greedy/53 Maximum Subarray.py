'''
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Example 2:
Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Greedy
        curMax = -math.inf
        maxSum = nums[0]
        
        for i in range(len(nums)):
            curMax = max(curMax + nums[i], nums[i])
            maxSum = max(maxSum, curMax)
        
        return maxSum