class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        
        # test case; [1,1,1,1,2,2,3], to be deleted: 3
        # nums after: [1, 1, 1, 1, 2, 2, 3]
        # from 0 to idx: [1, 1, 1, 1, 2, 2]
        
        
        return idx
