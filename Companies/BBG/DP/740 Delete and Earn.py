

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * (max(nums) + 1)
        for num in nums:
            dp[num] += num
        
        print(dp)

        # [2,2,3,3,3,4], total of 5 slots from 0 to 4
        #  0, 1, 2, 3, 4
        # [0, 0, 4, 9, 4]

        prev, curr = 0, 0
        for i in range(len(dp)):     
            oldCurr = curr
            curr = max(prev + dp[i], curr)
            prev = oldCurr
            
        return curr