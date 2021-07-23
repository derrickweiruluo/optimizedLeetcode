# Quick Sort 基操，模版级别


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quickSort(start, end):
            if start >= end:
                return
            left, right = start, end
            mid = left + (right - left + 1) // 2
            pivot = nums[mid]
            
            while left <= right:
                while left <= right and nums[left] < pivot: left += 1
                while left <= right and nums[right] > pivot: right -= 1
                # when left, right pointers stop moving
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
            
            quickSort(start, right)
            quickSort(left, end)
        
        quickSort(0, len(nums) - 1)
        return nums
