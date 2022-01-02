'''
nums is sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
'''


# O(N) 双指针
# input 是 sorted Non-Decreasing array

# 比较 左右两端，负数的平方可能大
# 根据两边的情况 move the index, index start from n - 1
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