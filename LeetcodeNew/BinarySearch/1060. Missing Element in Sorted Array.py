class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        if not nums or k == 0: 
            return 0
        
        diff = nums[-1] - nums[0] + 1. # complete length from [start_num: end_num]
        missing = diff - len(nums)
        if missing < k:
            return int(nums[-1] + (k - missing))
        
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            missing = nums[mid] - nums[0] - (mid - 0)
            if missing < k:
                left = mid + 1
            else:
                right = mid
        
        return nums[0] + k + left - 1   # at pos left, it is th result that has more than k spot, therefore, left - 1 at the end
