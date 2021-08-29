"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105

#######
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39743/Python-DP-solution-120ms
把最多两次交易想成： 第一次交易的解, profit 1代入到第二次购买，buy2 的成本为 price - profit1

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        one_buy = two_buy = math.inf
        one_profit = two_profit = 0
        
        for p in prices:
            one_buy = min(one_buy, p)
            one_profit = max(one_profit, p - one_buy)
            # 第二次买的时候，两次购买的花费，two_buy = p - one_profit
            two_buy = min(two_buy, p - one_profit)
            two_profit = max(two_profit, p - two_buy)
        
        return two_profit
