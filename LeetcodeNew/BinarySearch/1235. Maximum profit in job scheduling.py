'''
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.


https://leetcode.com/problems/maximum-profit-in-job-scheduling/

https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC%2B%2BPython-DP-Solution

Explanation
Sort the jobs by endTime.

dp[time] = profit means that within the first time duration,
we cam make at most profit money.
Intial dp[0] = 0, as we make profit = 0 at time = 0.

For each job = [s, e, p], where s,e,p are its start time, end time and profit,
Then the logic is similar to the knapsack problem.
If we don't do this job, nothing will be changed.
If we do this job, binary search in the dp to find the largest profit we can make before start time s.
So we also know the maximum cuurent profit that we can make doing this job.

Compare with last element in the dp,
we make more money,
it worth doing this job,
then we add the pair of [e, cur] to the back of dp.
Otherwise, we'd like not to do this job.


Complexity
Time O(NlogN) for sorting
Time O(NlogN) for binary search for each job
Space O(N)

Ex 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Ex 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
'''

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])  # sort the zipped tuple by endTime
        
        dp = [[0, 0]]  # end time, cur_end time profit 
        # dp to store at a given endTime, what is the max profix you can get, intialize at endTime = 0, 0 profit sofar
        
        # print(jobs)
        
        for start, end, profit in jobs:
            prevEndIdx = bisect.bisect_right(dp, [start + 1]) - 1
            # print(prevEndIdx)

            # the bottom up DP, jobs is sorted by endTime
            if dp[prevEndIdx][1] + profit > dp[-1][1]: 
                dp.append([end, dp[prevEndIdx][1] + profit])
        
        # print(dp)
        return dp[-1][1]