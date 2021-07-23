class Solution:
#   超低频，好的滑窗写法，preSum，模版
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def atMost(goal):
            if goal < 0: return 0
            preSum, pointer, res = 0, 0, 0
            for i in range(len(nums)):
                preSum += nums[i]
                while preSum > goal:
                    preSum -= nums[pointer]
                    pointer += 1
                res += i - pointer + 1
            return res
        
        return atMost(goal) - atMost(goal - 1)
