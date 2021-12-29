'''
一个从小到大sorted & rotated 的 array，含重复！！！！

找target 在不在里面

'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        n = len(nums)
        if nums[0] == target or nums[-1] == target: return True
        if nums[-1] < target < nums[0]: return False
        
        cutoff1, cutoff2 = n - 1, n - 1  # set to n - 1 because it may not be rotated
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                cutoff1, cutoff2 = i - 1, i
        
        def search(nums, l, r):
            left, right = l, r
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return nums[left] == target
        
        
        if target > nums[0]:    # search differnet part of the nums
            return search(nums, 0, cutoff1)
        else:
            return search(nums, cutoff2, n - 1)