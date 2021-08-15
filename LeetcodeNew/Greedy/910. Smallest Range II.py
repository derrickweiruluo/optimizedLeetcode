"""
You are given an integer array nums and an integer k.
For each index i where 0 <= i < nums.length, change nums[i] to be either nums[i] + k or nums[i] - k.
The score of nums is the difference between the maximum and minimum elements in nums.
Return the minimum score of nums after changing the values at each index.

Example 1:
Input: nums = [1], k = 0
Output: 0
Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

Example 2:
Input: nums = [0,10], k = 2
Output: 6
Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.

Example 3:
Input: nums = [1,3,6], k = 3
Output: 3
Explanation: Change nums to be [4, 6, 3]. The score is max(nums) - min(nums) = 6 - 3 = 3.
"""

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        res = nums[-1] - nums[0]
        
        for i in range(len(nums) - 1):
            candidates = [nums[0] + k, nums[i] + k, nums[i + 1] - k, nums[-1] - k]
            res = min(res, max(candidates) - min(candidates))
        
        return res
