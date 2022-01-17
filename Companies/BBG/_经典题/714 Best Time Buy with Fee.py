# 714. Best Time to Buy and Sell Stock with Transaction Fee
'''
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
'''

# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        '''You may not engage in multiple transactions simultaneously 
        (i.e., you must sell the stock before you buy again).'''

        profit = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            # ith day I do not own a share today (either did not have or sold today)
            profit = max(profit, hold + prices[i] - fee)
            
            # ith day I own a share today (either I already had or purchased tp=oday)
            hold = max(hold, profit - prices[i])
        
        
        return profit



# DP
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2: return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1[0] - prices[i]])
        
        return dp[n - 1][0]
