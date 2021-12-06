'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        idx = n - 1
        res = [0] * n
        
        left, right = 0, n - 1
        while left <= right:
            if nums[left] ** 2 >= nums[right] ** 2:
                res[idx] = nums[left] ** 2
                idx -= 1
                left += 1
            else:
                print(idx, right)
                res[idx] = nums[right] ** 2
                idx -= 1
                right -=1
        
        return res
                