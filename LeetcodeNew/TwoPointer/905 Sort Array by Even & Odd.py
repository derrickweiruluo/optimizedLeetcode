'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

'''


# BEST, O(N) time, inplace, O(1) space
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            if nums[i] % 2 == 1 and nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
            
            else:
                if nums[i] % 2 == 0:
                    i += 1
                if nums[j] % 2 == 1:
                    j -= 1
        
        return nums