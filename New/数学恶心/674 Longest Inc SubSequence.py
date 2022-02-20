'''
Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.


Input: nums = [2,2,2,2,2]
Output: 1
'''


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = i = 0  # left pointer starts at zero
        
        while i < len(nums):
            cur = 1
            while i + 1 < len(nums) and nums[i] < nums[i + 1]:
                cur += 1
                i += 1
            res = max(res, cur)
            i += 1
        
        return res