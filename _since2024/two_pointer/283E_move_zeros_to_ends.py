class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        ex1: [1,0,1,0]
        idx = 0, slow = 0
        idx = 1, s

        ex2: [0,0,1,1]
        idx = 0, 1.....
        slow = 0, 1.....
        idx = 2, slow = 2 -> [1,0,0,1]
        idx = 3, slow = 3 -> [1,1,0,0]
        """
        slow_pointer_for_zero = 0 # next swapping position, which is towards the end of the array
        for i, num in enumerate(nums):
            # both if may get triggered
            if num != 0 and nums[slow_pointer_for_zero] == 0:
                nums[i], nums[slow_pointer_for_zero] = nums[slow_pointer_for_zero], nums[i]
            # slow pointer is updated after swapping
            if nums[slow_pointer_for_zero] != 0:
                slow_pointer_for_zero += 1
