'''
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Ex1 :

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

'''


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        dp = [[0, 0]]
        
        for start, end, profit in jobs:
            nextIdx = bisect.bisect_right(dp, [start + 1]) - 1
            if dp[nextIdx][1] + profit > dp[-1][1]:
                dp.append([end, dp[nextIdx][1] + profit])
                
        
        return dp[-1][1]