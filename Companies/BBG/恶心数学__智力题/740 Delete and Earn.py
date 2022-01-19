'''
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.
'''

# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.

# Input: nums = [2,2,3,3,3,4]
# Output: 9


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        prev, cur = 0, 0
        for val in range(max(nums) + 1):
        # for val in range(min(nums)-1, max(nums) + 1):
            prev, cur = cur, max(prev + val * counter[val], cur)
        
        return cur



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