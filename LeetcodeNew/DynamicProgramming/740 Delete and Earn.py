'''
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Ex 1:
Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Ex 2:
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: Delete all threes and get 9, (2, 4) are skipped
'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * (max(nums) + 1)
        for num in nums:
            dp[num] += num
        
        print(dp)
        prev, curr = 0, 0
        for i in range(len(dp)):
            # print("BEFORE", prev, curr)
            # prev, curr = curr, max(prev + dp[i], curr)
            # print("AFTER",  prev, curr)
            
            oldCurr = curr
            curr = max(prev + dp[i], curr)
            prev = oldCurr
            
        return curr