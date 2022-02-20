'''
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

# Clarifications:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        sell, cooldown, hold = 0, -math.inf, -math.inf
        
        for p in prices:
            hold = max(hold, sell - p)
            sell = max(sell, cooldown)
            cooldown = hold + p
        
        return max(sell, cooldown)