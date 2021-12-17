'''
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

'''
# 找零钱，assume input有的coin种类有无数个
# 返回：用最少数量的硬币找零
# if fail, return -1

'''
It's actually a complete backpack problem:

capacity of the "backpack" is amount
coins represents value of each item you can put into the "backpack"
you can take 0 or many coins
for each coin the cost is constant 1
so the question is to find minimum cost to fill the "backpack"
'''

'''
"""
解题方法
动态规划
题目比较重要的是硬币无限数量。我们的做法是使用动态规划，需要构建一个长度是amount + 1的dp数组，
其含义是能够成面额从0到amount + 1需要使用的最少硬币数量。
所以我们对每一种面额的硬币，都去计算并更新新添了这种面额的情况下，构成的所有面额需要的最少硬币数量。注意，变量是不同面额的硬币。
dp更新的策略是从coin面额到amount+1的面额依次向后查找，看这个位置能不能用更少的硬币组成（即使用面额是i - coin的需要硬币数量+1).
"""
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [math.inf] * amount
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
                
        return dp[amount] if dp[amount] != math.inf else -1