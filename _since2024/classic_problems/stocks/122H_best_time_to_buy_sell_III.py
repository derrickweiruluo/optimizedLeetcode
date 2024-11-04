"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        CONDITION:  On each day, you may decide to buy and/or sell the stock. 
        You can only hold at most one share of the stock at any time. 
        However, you can buy it then immediately sell it on the same day.
        同一天，先卖掉，在买回来
        """
        if len(prices) == 0:
            return 0
        
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        
        return res
    
    
    