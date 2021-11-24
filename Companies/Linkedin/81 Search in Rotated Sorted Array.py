'''
一个从小到大sorted & rotated 的 array，含重复！！！！

找target 在不在里面

'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        n = len(nums)
        
        if target == nums[0] or target == nums[-1]: return True
        if nums[-1] < target < nums[0]: return False
        
        cutoff1, cutoff2 = n -1, n - 1
        for i in range (n - 1):
            if nums[i + 1] < nums [i]:
                cutoff1, cutoff2 = i, i + 1
        
        def search(l, r):
            left, right = l, r
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return nums[left] == target
        
        # print(cutoff1, cutoff2)
        if target > nums[0]:
            return search(0, cutoff1)
        else:
            return search (cutoff2, n - 1)