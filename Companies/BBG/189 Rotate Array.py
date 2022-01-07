'''
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2: return
        k = k % n
        
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        reverse(nums, 0, n - k - 1)
        reverse(nums, n - k, n - 1)
        reverse(nums, 0, n - 1)
        
        # [1,2,3,4,5,6,7]  k = 3 ==> target: [5,6,7,1,2,3,4]
        # -> [1,2,3,4] --> [4,3,2,1]
        # -> [5,6,7]   --> [7,6,5]
        # -->[4,3,2,1,7,6,5]  --> [5,6,7,1,2,3,4]