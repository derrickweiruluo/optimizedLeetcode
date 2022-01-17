'''
Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.



Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
day_1 + cost(1-day) + day_3 + cost(7-days) + day_20 + cost(1-day)
'''


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [0] * (days[-1] + 1)  # dp of cost from day 0 to the last day inclusive
        days = set(days)           # for O(1) look up
        
        for i in range(len(dp)):
            if i not in days:
                dp[i] = dp[i - 1]   # if ith day is not need, == i - 1
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0], \
                            dp[max(0, i - 7)] + costs[1], \
                            dp[max(0, i - 30)] + costs[2])
        
        return dp[-1] 