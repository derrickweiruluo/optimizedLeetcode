"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

"""

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 这题的关键是切分数组，每个都要非空且最大subarray之和要被最小化
        # 等同于最小化地切分weighted蛋糕块

        def isValidCut(nums, target):
            """
            isValid == True: the try-number is too large but valid, move right to this `target`,
            isValid == False: the try-number is invalid, move left `target + 1`
            """
            count = 1
            current_sum = 0
            for num in nums:
                current_sum += num
                if current_sum > target:
                    count += 1
                    current_sum = num
                if count > k:
                    return False
            return True

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2
            if isValidCut(nums, mid):
                right = mid
            else:
                left = mid + 1
        return left
