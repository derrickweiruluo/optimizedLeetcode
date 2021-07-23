class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dist = 0
        for i, increment in enumerate(nums):   #高光1
            if max_dist < i : return False
            max_dist = max(max_dist, i + increment)
        return True
