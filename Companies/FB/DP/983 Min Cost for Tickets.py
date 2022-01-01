'''
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.ß

'''

# Example: 
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total, you spent $11 and covered all the days of your travel.

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [0] * (days[-1] + 1) # dp from day 0 to the last day
        
        
        for i in range(1, days[-1] + 1):  # "i" is the calendar day
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                           dp[max(0, i - 7)] + costs[1],
                           dp[max(0, i - 30)] + costs[2])
        
        return dp[days[-1]]