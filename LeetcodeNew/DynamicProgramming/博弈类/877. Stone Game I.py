'''
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.
Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.


Example 1:

Input: piles = [5,3,4,5]
Output: true

DP 2D Matrix

    0   1   2   3
------------------------
0   L1  L2  L3  L4

1       L1  L2  L3

2           L1  L2

3               L1

https://www.youtube.com/watch?v=WxpIHvsu1RI

'''

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = piles[i]
        
        # diagonal traversal of 2D array
        for dist in range(1, n):
            for i in range(n - dist):
                j = i + dist
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        
        
        return dp[0][n-1] > 0